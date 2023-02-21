inp = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]
graph = []

for i in range(len(inp)):
    temp = []
    for j in range(len(inp)):
        temp.append(0)
    graph.append(temp)

for (u, v) in inp:
    graph[u][v] = 1  # if there is edge then connect the two vertices
    graph[v][u] = 1  # also connect both ways as this undirected graph
    # if the graph is directed then do not connect both ways

print("The generated graph in form of adjacency matrix is :")
for i in graph:
    print(i)
