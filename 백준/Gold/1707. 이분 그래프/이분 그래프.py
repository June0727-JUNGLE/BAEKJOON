from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS_recursion(start, col):
    visited[start] = col
    for v in graph[start]:
        if visited[v] == 0:
            if DFS_recursion(v, -col):
                return True
        elif visited[v] == col:
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

        visited = [0] * (V+1)
        result = False

        for i in range(1, V+1):
            if visited[i] == 0:
                if DFS_recursion(i, 1):
                    result = True
                    break

        print("NO" if result else "YES")
