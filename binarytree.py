class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Create binary tree
    def create_tree(self):
        val = int(input("Enter value (-1 for no node): "))

        if val == -1:
            return None

        node = Node(val)

        print("Enter left child of", val)
        node.left = self.create_tree()

        print("Enter right child of", val)
        node.right = self.create_tree()

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
tree = BinaryTree()

print("Create Binary Tree")
tree.root = tree.create_tree()

print("\nInorder Traversal:")
tree.inorder(tree.root)

print("\nPreorder Traversal:")
tree.preorder(tree.root)

print("\nPostorder Traversal:")
tree.postorder(tree.root)