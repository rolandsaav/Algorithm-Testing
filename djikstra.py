import heapq

edges = [
    [0, 1, 4],
    [0, 2, 2],

    [1, 2, 3],
    [1, 3, 2],
    [1, 4, 3],

    [2, 1, 1],
    [2, 3, 4],
    [2, 4, 5],

    [4, 3, 1]
]

n = 5

# This essentially prepopulates the graph with the proper number of edgeless nodes
# Doing this ensures we don't have missing indices
adjGraph = {i:[] for i in range(n)}

for a, b, weight in edges:    
    adjGraph[a].append((b, weight))

def djikstra(source, graph):
    distances = [float('inf') for i in range(len(graph))]
    visited = set()
    predMap = {source: source}
    distances[source] = 0
    minHeap = [(0, source)]
    heapq.heapify(minHeap)

    while len(minHeap) > 0:
        curDist, current = heapq.heappop(minHeap)

        if current in visited:
            continue

        visited.add(current)

        for nbr, weight in graph[current]:
            if distances[nbr] > distances[current] + weight:
                distances[nbr] = distances[current] + weight
                predMap[nbr] = current
            heapq.heappush(minHeap, (distances[nbr], nbr))
    
    return distances, predMap

distances, predecessors = djikstra(0, adjGraph)

def createPathFromPredecessors(source, predecessors):
    if source == predecessors[source]:
        return [source]
    
    path = [source]
    path.extend(createPathFromPredecessors(predecessors[source], predecessors))

    return path

path = createPathFromPredecessors(4, predecessors)
path.reverse()
print(path)