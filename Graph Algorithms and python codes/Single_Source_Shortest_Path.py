inp = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['D', 'G'], ['G', 'I'], ['G', 'H'], ['C', 'E'], ['C', 'F']]
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# generating graph
graph = {}
for i in nodes:
    graph[i] = []

for (u, v) in inp:
    graph[u].append(v)
    graph[v].append(u)


def single_source_shortest_path(graph, node, parent_node, distance, d):
    distance[node] = d

    for child_node in graph[node]:
        if child_node != parent_node:
            single_source_shortest_path(graph, child_node, node, distance, distance[node] + 1)


start = 'A'  # taking node 'A' as starting node
distance = dict()
distance[start] = 0  # distance of starting node is zero

# function calling
single_source_shortest_path(graph, start, -1, distance, 0)

# printing corresponding distance
for i, j in distance.items():
    print(i, j)
