class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    new = Node(data)

    if root is None:
        return new

    temp = root

    while True:
        if data < temp.data:
            if temp.left is None:
                temp.left = new
                break
            temp = temp.left
        else:
            if temp.right is None:
                temp.right = new
                break
            temp = temp.right

    return root


# Non-recursive Inorder
def inorder(root):
    stack = []
    temp = root

    while stack or temp:
        while temp:
            stack.append(temp)
            temp = temp.left

        temp = stack.pop()
        print(temp.data, end=" ")
        temp = temp.right


# Non-recursive Preorder
def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        temp = stack.pop()
        print(temp.data, end=" ")

        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)


# User Input
root = None

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    root = insert(root, roll)

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)