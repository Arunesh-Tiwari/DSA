inp = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]
graph = {}  # create a dictionary

for i in range(len(inp)):
    graph[i] = []  # allocating an empty list to each node

for (u, v) in inp:
    graph[u].append(v)  # appending the connected vertices
    graph[v].append(u)  # appending the connected vertices

print("The generated graph in form of adjacency list is :")
for i in graph.items():
    print(i)
