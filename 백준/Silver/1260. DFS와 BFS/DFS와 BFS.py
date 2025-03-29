import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

def dfs_recursive(graph, node):
    res = []
    visited = set()

    def _dfs(k):
        res.append(k)
        visited.add(k)
        for l in graph[k]:
            if l not in visited:
                _dfs(l)

    _dfs(node)
    return res

def bfs_queue(graph, node):
    res = []
    queue = [node]
    visited = set(queue)
    while queue:
        u = queue.pop(0)
        res.append(u)
        for v in graph[u]:
            if v not in visited:
                queue.append(v)
                visited.add(v)
    return res

print(*dfs_recursive(graph, V))
print(*bfs_queue(graph, V))