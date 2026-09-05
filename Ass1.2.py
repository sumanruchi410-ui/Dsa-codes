stack = [None] * 5
top = -1
size = 5

while True:
    print("\n--- Library Book Stack ---")
    print("1. Return Book (Push)")
    print("2. Arrange Book (Pop)")
    print("3. Top Book (Peek)")
    print("4. Display Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Push
    if choice == 1:
        if top == size - 1:
            print("Stack Overflow!")
        else:
            book = input("Enter book name: ")
            top = top + 1
            stack[top] = book
            print("Book returned successfully.")

    # Pop
    elif choice == 2:
        if top == -1:
            print("Stack Underflow!")
        else:
            print("Book arranged:", stack[top])
            stack[top] = None
            top = top - 1

    # Peek
    elif choice == 3:
        if top == -1:
            print("Stack is empty!")
        else:
            print("Top book:", stack[top])

    # Display
    elif choice == 4:
        if top == -1:
            print("Stack is empty!")
        else:
            print("Books in stack:")
            i = top
            while i >= 0:
                print(stack[i])
                i = i - 1

    # Exit
    elif choice == 5:
        break

    else:
        print("Invalid choice!")