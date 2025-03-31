import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topl_sort(graph):
    res = []
    que = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            que.append(i)
    while que:
        u = que.popleft()
        res.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                que.append(v)
    return res

result = topl_sort(graph)
print(*result)