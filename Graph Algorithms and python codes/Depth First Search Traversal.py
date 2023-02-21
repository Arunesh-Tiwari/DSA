inp = [[1, 2], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [4, 6], [5, 6]]
graph = {}

# generating graph
for i in range(len(inp)):
    graph[i] = []

for (u, v) in inp:
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, node, visited=set()):
    print(node, end=" ")
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph, child, visited)


dfs(graph, 1)  # dfs function call
