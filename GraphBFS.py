n = int(input("Enter number of vertices: "))
graph = [[] for i in range(n)]

e = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for i in range(e):
    edge = input().split()
    u = int(edge[0])
    v = int(edge[1])
    graph[u] = graph[u] + [v]
    graph[v] = graph[v] + [u]

start = int(input("Enter starting vertex: "))

visited = [0] * n
queue = [0] * n
front = 0
rear = 0

queue[rear] = start
rear = rear + 1
visited[start] = 1

print("BFS Traversal:", end=" ")

while front < rear:
    current = queue[front]
    front = front + 1
    print(current, end=" ")

    j = 0
    while j < len(graph[current]):
        v = graph[current][j]

        if visited[v] == 0:
            queue[rear] = v
            rear = rear + 1
            visited[v] = 1

        j = j + 1

print()