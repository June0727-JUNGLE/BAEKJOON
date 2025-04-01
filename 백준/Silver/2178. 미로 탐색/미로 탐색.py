import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0<= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[cx][cy]+1
                    queue.append((nx, ny))
bfs(0, 0)
print(visited[N-1][M-1])