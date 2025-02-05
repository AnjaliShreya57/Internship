import csv

def load_dataset(file_path):
    """Load data from a CSV file."""
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def analyze_dataset(data):
    """Basic data analysis and summary."""
    if data:
        keys = data[0].keys()
        print("\nData Summary:")
        for key in keys:
            values = [float(row[key]) for row in data if row[key].replace('.', '', 1).isdigit()]
            print(f"{key} - Min: {min(values)}, Max: {max(values)}, Mean: {sum(values)/len(values)}")

def visualize_dataset(data, column_x, column_y):
    """Generate a simple text-based scatter plot."""
    print(f"\nText-based Scatter Plot for {column_x} vs {column_y}:\n")
    x_values = [float(row[column_x]) for row in data if row[column_x].replace('.', '', 1).isdigit()]
    y_values = [float(row[column_y]) for row in data if row[column_y].replace('.', '', 1).isdigit()]

    for x, y in zip(x_values, y_values):
        # Display a very basic scatter plot using text
        print(f"({x}, {y})")

def main():
    file_path = "pandaaster.csv"  # Hardcoded file path
    data = load_dataset(file_path)
    if data is not None:
        analyze_dataset(data)
        col_x = input("Enter column name for X-axis visualization: ")
        col_y = input("Enter column name for Y-axis visualization: ")
        if col_x in data[0] and col_y in data[0]:
            visualize_dataset(data, col_x, col_y)
        else:
            print("Invalid column names.")

if __name__ == "__main__":
    main()
