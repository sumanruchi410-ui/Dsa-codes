# DFS using Adjacency Matrix

# Number of vertices
n = int(input("Enter number of vertices: "))

# Create adjacency matrix
graph = []

print("Enter adjacency matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


# Visited array
visited = [0] * n


# DFS function
def dfs(v):
    print(v, end=" ")
    visited[v] = 1

    for i in range(n):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)


# Starting vertex
start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(start)