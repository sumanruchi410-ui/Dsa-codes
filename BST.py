class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a value into BST
    def insert(self, node, val):
        if node is None:
            return Node(val)

        if val < node.val:
            node.left = self.insert(node.left, val)

        elif val > node.val:
            node.right = self.insert(node.right, val)

        else:
            print("Duplicate value not allowed!")

        return node

    # Inorder: Left -> Root -> Right
    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.val, end=" ")
        self.inorder(node.right)

    # Preorder: Root -> Left -> Right
    def preorder(self, node):
        if node is None:
            return

        print(node.val, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    # Postorder: Left -> Right -> Root
    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end=" ")


# Main program
tree = BinarySearchTree()

n = int(input("Enter number of nodes: "))

print("Enter values:")
for i in range(n):
    val = int(input("Enter value: "))
    tree.root = tree.insert(tree.root, val)


# User chooses traversal
print("\nChoose Traversal:")
print("1. Inorder")
print("2. Preorder")
print("3. Postorder")
print("4. All Three")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Inorder Traversal:")
    tree.inorder(tree.root)

elif choice == 2:
    print("Preorder Traversal:")
    tree.preorder(tree.root)

elif choice == 3:
    print("Postorder Traversal:")
    tree.postorder(tree.root)

elif choice == 4:
    print("Inorder Traversal:")
    tree.inorder(tree.root)

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)

    print("\nPostorder Traversal:")
    tree.postorder(tree.root)

else:
    print("Invalid choice!")