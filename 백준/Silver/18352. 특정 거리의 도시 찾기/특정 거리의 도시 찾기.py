import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def bfs(graph, start, target):
    queue = deque([(start, 0)])
    visited = set([start])
    res = []

    while queue:
        u, dist = queue.popleft()

        if dist == target:
            res.append(u)
        elif dist < target:
            for v in graph[u]:
                if v not in visited:
                    queue.append((v, dist + 1))
                    visited.add(v)

    if not res:
        return [-1]
    else:
        res.sort()
        return res

for city in bfs(graph, X, K):
    print(city)
