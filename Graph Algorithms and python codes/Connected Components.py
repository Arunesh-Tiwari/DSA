edges = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['D', 'E'], ['B', 'E'], ['F', 'H'], ['F', 'G'], ['I', 'J']]
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

graph = {}
# generating graph
for i in range(len(nodes)):
    graph[nodes[i]] = []

for (u, v) in edges:
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, node, visited):
    # print(node, end=" ")
    visited.add(node)
    summ = 0  # summ is to count the number of connected nodes
    for child in graph[node]:
        if child not in visited:
            summ += dfs(graph, child, visited)  # function call is the child is not visited
    return summ + 1


ans = []
visited = set()  # to monitor already visited nodes
for items in nodes:
    if items not in visited:
        temp = dfs(graph, items, visited)  # function call for dfs traversal
        ans.append(temp)
print(ans)  # printing number of connected components
