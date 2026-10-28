n = int(input("Enter number of vertices: "))

if n <= 0 or n > 100:
    print("Enter a number of vertices from 1 to 100.")
else:
    cost = [[0 for j in range(n)] for i in range(n)]

    e = int(input("Enter number of edges: "))

    for i in range(e):
        print("Enter source and destination:")
        u = int(input())
        v = int(input())

        u = u - 1
        v = v - 1

        if u >= 0 and u < n and v >= 0 and v < n:
            cost[u][v] = 1
            cost[v][u] = 1
        else:
            print("Invalid vertex number.")

    stack = [0 for i in range(n)]
    top = -1

    print("Adjacency matrix:")
    for i in range(n):
        for j in range(n):
            print(cost[i][j], end=" ")
        print()

    print("Stack:")
    for i in range(n):
        print(stack[i], end=" ")
    print()

    print("Top:", top)