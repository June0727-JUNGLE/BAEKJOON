import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

def dfs_recur(graph, node):
    visited = set()
    def _dfs(k):
        if k in visited:
            return
        visited.add(k)
        for l in graph[k]:
            if l not in visited:
                _dfs(l)
    _dfs(node)
    return len(visited)

print(dfs_recur(graph, 1)-1)