# Library Catalog Navigation using Binary Tree

# Node of the Binary Tree
class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


# Inorder Traversal: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.book, end=" ")
        inorder(root.right)


# Preorder Traversal: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.book, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.book, end=" ")


# Creating the library catalog
root = Node("DSA")
root.left = Node("Python")
root.right = Node("DBMS")

root.left.left = Node("C Programming")
root.left.right = Node("Java")

root.right.left = Node("Operating Systems")
root.right.right = Node("Computer Networks")


# Displaying different navigation sequences
print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)