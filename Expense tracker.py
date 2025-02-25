import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from datetime import datetime

# Database Initialization
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
''')
conn.commit()


# Function to Add Expense
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_combobox.get()
        description = description_entry.get()
        date = datetime.now().strftime("%Y-%m-%d")

        if not category or not description:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                       (amount, category, description, date))
        conn.commit()
        messagebox.showinfo("Success", "Expense added successfully!")
        clear_inputs()
        view_expenses()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")


# Function to View Expenses
def view_expenses():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


# Function to Show Monthly Summary
def show_summary():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    if not categories:
        messagebox.showinfo("No Data", "No expenses found.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.title("Expense Breakdown")
    plt.show()


# Function to Clear Input Fields
def clear_inputs():
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    category_combobox.set("")


# GUI Setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Labels and Input Fields
tk.Label(root, text="Amount ($):", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Category:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Others"]
category_combobox = ttk.Combobox(root, values=categories, state="readonly")
category_combobox.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Description:", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
description_entry = tk.Entry(root)
description_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Show Summary", command=show_summary, bg="#2196F3", fg="white", font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=10)

# Table for Expense List
tree = ttk.Treeview(root, columns=("ID", "Amount", "Category", "Description", "Date"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Amount", text="Amount ($)")
tree.heading("Category", text="Category")
tree.heading("Description", text="Description")
tree.heading("Date", text="Date")
tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

view_expenses()

root.mainloop()
