class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Non-recursive Inorder
def inorder(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


# Non-recursive Preorder
def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.data, end=" ")

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


# Main
root = None

n = int(input("Enter number of nodes: "))

print("Enter the elements:")
for i in range(n):
    data = int(input())
    root = insert(root, data)

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)