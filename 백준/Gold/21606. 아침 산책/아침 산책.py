import sys 
from collections import deque
input = sys.stdin.readline

N = int(input())
place = [0] + list(map(int, input().strip()))
graph = [[]for _ in range(N+1)]
for _ in range(N-1):
    u ,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0

def dfs(node, graph):
    global cnt
    stk = deque([node])
    visited = set([node])

    while stk:
        j = stk.pop()
        for k in graph[j]:
            if k not in visited:                
                if place[k] == 1:
                    cnt += 1
                    continue
                else:
                    visited.add(k)
                    stk.append(k)

for i in range(1, N+1):
    if place[i] == 0:
        continue
    else:
        dfs(i, graph)

print(cnt)