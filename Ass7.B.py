# Road Network Exploration
# DFS using Adjacency Matrix

# Number of intersections
n = int(input("Enter number of intersections: "))

# Create adjacency matrix
graph = []

print("Enter the road network adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Visited array
visited = [0] * n


# DFS function
def dfs(vertex):
    print(vertex, end=" ")
    visited[vertex] = 1

    for i in range(n):
        if graph[vertex][i] == 1 and visited[i] == 0:
            dfs(i)


# Starting intersection
start = int(input("Enter starting intersection: "))

print("Intersections visited using DFS:")
dfs(start)