
# Graph should be an n x n adjacency matrix
from typing import Union, List

m = [
    [0, 4, 1, 9],
    [3, 0, 6, 11],
    [4, 1, 0, 2],
    [6, 5, -4, 0]
]


def floyd_warshall(graph):
    n = len(graph)

    # n x n dp matrix. Final state will store shortest path lengths. Initally empty
    dp: List[List[Union[float, int]]] = [[0 for _ in range(n)] for _ in range(n)]

    # n x n matrix of initially null values
    nextNodes: List[List[Union[None, int]]] = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dp[i][j] = graph[i][j]
            if graph[i][j] != float("inf"):
                nextNodes[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    nextNodes[i][j] = nextNodes[i][k]

    return dp, nextNodes

def getPath(start, end, m):
    path = []
    if m[start][end] == float("inf"):
        return path

    cur = start
    while cur != end:
        path.append(cur)
        cur = m[cur][end]
    path.append(cur)
    return path


shortestDistances, paths = floyd_warshall(m)

for row in paths:
    print(row)

print()

for row in shortestDistances:
    print(row)

print()

print(getPath(0, 3, paths))
