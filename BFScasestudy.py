n = int(input("Enter number of users: "))
graph = [[] for i in range(n)]

e = int(input("Enter number of friendships: "))

for i in range(e):
    u, v = input("Enter friendship (u v): ").split()
    u = int(u)
    v = int(v)
    graph[u] = graph[u] + [v]
    graph[v] = graph[v] + [u]

start = int(input("Enter starting user: "))

visited = [0] * n
queue = [start]
visited[start] = 1
front = 0
level = 0

while front < len(queue):
    size = len(queue) - front
    print("Level", level, end=": ")

    for i in range(size):
        current = queue[front]
        front = front + 1
        print(current, end=" ")

        j = 0
        while j < len(graph[current]):
            v = graph[current][j]

            if visited[v] == 0:
                visited[v] = 1
                queue = queue + [v]

            j = j + 1

    print()
    level = level + 1

