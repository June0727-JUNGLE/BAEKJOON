from collections import deque
import sys
input = sys.stdin.readline

def DFS(start, col):
    stk = deque([start])
    visited[start] = col

    while stk:
        u = stk.pop()
        for v in graph[u]:
            if not visited[v]:
                stk.append(v)
                visited[v] = -visited[u]
            elif visited[v] == visited[u]:
                return True
    return False   

if __name__ == "__main__":
    K = int(input())

    for _ in range(K):
        V, E = map(int, input().split())

        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (V+1)

        for i in range(1, V+1):
            if not visited[i]:
                result = DFS(i, 1)
                if result:
                    print("NO")
                    break
        else:
            print("YES")