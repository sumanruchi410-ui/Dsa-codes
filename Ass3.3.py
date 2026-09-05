# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Display
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head

            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("NULL")


# Create empty linked list
ll = SinglyLinkedList()

while True:
    print("\n- College Library -")
    print("1. Insert at Beginning")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter Book ID: "))
        ll.insert_begin(value)
        print("Book ID inserted successfully.")

    elif choice == 2:
        ll.display()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")