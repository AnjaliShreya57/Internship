def count_words(text):
    """Counts the number of words in a given text."""
    words = text.split()  # Splitting text into words
    return len(words)

def main():
    """Main function to handle user input and display output."""
    text = input("Enter a sentence or paragraph: ").strip()
    
    if not text:
        print("Error: No input provided. Please enter some text.")
        return

    word_count = count_words(text)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
def count_words(text):
    """Counts the number of words in a given text."""
    words = text.split()  # Splitting text into words
    return len(words)

def main():
    """Main function to handle user input and display output."""
    text = input("Enter a sentence or paragraph: ").strip()
    
    if not text:
        print("Error: No input provided. Please enter some text.")
        return

    word_count = count_words(text)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
