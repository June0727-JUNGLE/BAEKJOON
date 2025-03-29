import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[]for _ in range(N+1)]

for _ in range(1, N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def find_parent(graph, node):
    que = deque([node])
    visited = set([node])
    parent = [[] for _ in range(N+1)]
    while que:
        u = que.popleft()
        for v in graph[u]:
            if v not in visited:
                parent[v] = u
                que.append(v)
                visited.add(v)
    return parent

parents = find_parent(graph, 1)
for i in range(2, N+1):
    print(parents[i])