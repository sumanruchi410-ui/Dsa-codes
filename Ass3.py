class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print("Book ID", value, "inserted.")

    # Display Linked List
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("NULL")


# Main Program
library = SinglyLinkedList()

while True:
    print("\n----- College Library Menu -----")
    print("1. Insert at Beginning")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter Book ID: "))
        library.insert_begin(value)

    elif choice == 2:
        library.display()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")