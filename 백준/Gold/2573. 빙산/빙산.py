import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
time = 0
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque([(x,y)])
    visited[x][y] = 1
   
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (0 <= nx < N and 0 <= ny < M):
                if graph[nx][ny] == 0:  # 현 위치 주변이 바다
                    visited[cx][cy] += 1  # 바다 개수 저장

            if visited[nx][ny] == 0 and graph[nx][ny] != 0:  # 현 위치 주변이 빙산
                queue.append((nx, ny))
                visited[nx][ny] = 1

    
            
   
while True:
    count = 0
    visited = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and visited[i][j] == 0:
                bfs(i, j)
                count += 1
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                graph[i][j] -= (visited[i][j] - 1)
                if graph[i][j] < 0:
                    graph[i][j] = 0
                        
    if count >= 2:
        print(time)
        break
    if count == 0:
        print(0)
        break   
    
    time += 1
