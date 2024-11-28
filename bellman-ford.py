# edges of the form (u, v, w)
edges = [
    [0, 1, 10],
    [0, 5, 8],
    [1, 3, 2],
    [2, 1, 1],
    [3, 2, -2],
    [4, 1, -4],
    [4, 3, -1],
    [5, 4, 1]
]

n = 6
adjGraph = {i:[] for i in range(n)}

for a, b, weight in edges:
    adjGraph[a].append((b, weight))

# TC: O(V*E)
def bellman_ford(source, graph):
    n = len(graph)
    distances = [float('inf') for _ in range(n)]
    distances[source] = 0
    
    # This essentially loops for the number of vertices
    for _ in range(n - 1):
        # These inner two loops loop over all the edges
        for u in graph:
            for v, w in graph[u]:
                distances[v] = min(distances[v], distances[u] + w)
    
    return distances

print(bellman_ford(0, adjGraph))