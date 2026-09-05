queue = [None] * 5
front = -1
rear = -1
size = 5

while True:
    print("\n--- Ticket Booking Queue ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Enqueue
    if choice == 1:
        if rear == size - 1:
            print("Queue Overflow!")
        else:
            ticket = input("Enter customer name: ")

            if front == -1:
                front = 0

            rear = rear + 1
            queue[rear] = ticket

            print("Customer added to queue.")

    # Dequeue
    elif choice == 2:
        if front == -1 or front > rear:
            print("Queue Underflow!")
        else:
            print("Customer served:", queue[front])
            queue[front] = None
            front = front + 1

            if front > rear:
                front = -1
                rear = -1

    # Display
    elif choice == 3:
        if front == -1:
            print("Queue is empty!")
        else:
            print("Customers in queue:")
            i = front

            while i <= rear:
                print(queue[i])
                i = i + 1

    # Exit
    elif choice == 4:
        break

    else:
        print("Invalid choice!")