#:- Ruchi Suman
# Roll no:- 44 Div:- SY5
# Batch B

class Stack:
    def __init__(self):
        # Pre-filled stack
        self.books = [
        "Python Basics",
        "Data Structures",
        "Operating Systems"
        ]

    # Return Book (Push)
    def return_book(self, book):
        self.books.append(book)
        print(f'"{book}" returned successfully.')

    # Arrange Book (Pop)
    def arrange_book(self):
        if len(self.books) == 0:
            print("No books to arrange.")
        else:
            book = self.books.pop()
            print(f'"{book}" arranged on the shelf.')

    # Top Book (Peek)
    def top_book(self):
        if len(self.books) == 0:
            print("Stack is empty.")
        else:
            print("Top Book:", self.books[-1])

    # Display Stack
    def display(self):
        if len(self.books) == 0:
            print("No returned books.")
        else:
            print("Returned Books (Top to Bottom):")
            for book in reversed(self.books):
                print(book)


# Main Program
stack = Stack()

while True:
    print("\n--- Library Returned Books Stack ---")
    print("1. Return Book")
    print("2. Arrange Book")
    print("3. Top Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        stack.return_book(book)

    elif choice == 2:
        stack.arrange_book()

    elif choice == 3:
        stack.top_book()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")