class Queue:
    def __init__(self, size):
        self.queue = [0] * size
        self.front = -1
        self.rear = -1
        self.size = size

    # Enqueue Operation
    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue Overflow! No more tickets can be booked.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(item, "added to the queue.")

    # Dequeue Operation
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow! No customers in the queue.")
        else:
            print(self.queue[self.front], "removed from the queue.")
            self.front += 1

            if self.front > self.rear:
                self.front = -1
                self.rear = -1

    # Display Operation
    def display(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Customers in the queue:")
            i = self.front
            while i <= self.rear:
                print(self.queue[i], end=" ")
                i += 1
            print()


# Main Program
size = int(input("Enter queue size: "))
q = Queue(size)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer = input("Enter customer name: ")
        q.enqueue(customer)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")