class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
def create():
    n = int(input("Enter number of nodes: "))

    nodes = {}

    # Enter node values
    for i in range(n):
        data = int(input("Enter node " + str(i + 1) + ": "))
        nodes[data] = Node(data)

    # Enter children
    for i in range(n):
        parent = int(input("\nEnter parent node: "))

        left = int(input("Enter left child (-1 for none): "))
        right = int(input("Enter right child (-1 for none): "))

        if left != -1:
            nodes[parent].left = nodes[left]

        if right != -1:
            nodes[parent].right = nodes[right]

    # Enter root
    root_value = int(input("\nEnter root node: "))

    return nodes[root_value], n


# Non-Recursive Inorder Traversal
# Left -> Root -> Right
def inorder(root, n):

    stack = [None] * n
    top = -1
    PTR = root

    print("\nInorder Traversal: ", end="")

    while PTR != None or top != -1:

        # Go to leftmost node
        while PTR != None:
            top = top + 1
            stack[top] = PTR
            PTR = PTR.left

        # Remove from stack
        PTR = stack[top]
        top = top - 1

        # Visit node
        print(PTR.data, end=" ")

        # Move to right child
        PTR = PTR.right


# Main
root, n = create()

inorder(root, n)