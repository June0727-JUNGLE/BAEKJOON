import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

def dfs_stk(graph, node, visited):
    stk = [node]
    visited.add(node)
    while stk:
        u = stk.pop()
        for v in graph[u]:
            if v not in visited:
                stk.append(v)
                visited.add(v)

visited = set()
cnt = 0

for i in range(1, N+1):
    if i not in visited:
        dfs_stk(graph, i, visited)
        cnt += 1

print(cnt)