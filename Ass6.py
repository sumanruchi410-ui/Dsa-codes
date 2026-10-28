class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Print tree level-wise
def level_order(root):
    if root is None:
        return

    queue = [root]
    front = 0

    while front < len(queue):
        current = queue[front]
        front = front + 1

        print(current.data, end=" ")

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


# Find height of BST
def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


# Print leaf nodes
def print_leaf_nodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")

    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)


# Main program
root = None

n = int(input("Enter number of employees: "))

print("Enter employee IDs:")

i = 0
while i < n:
    emp_id = int(input("Enter ID: "))
    root = insert(root, emp_id)
    i = i + 1


# Original BST
print("\nOriginal BST level-wise:")
level_order(root)


# Height
print("\n\nHeight of BST:", height(root))


# Leaf nodes
print("Leaf nodes:")
print_leaf_nodes(root)