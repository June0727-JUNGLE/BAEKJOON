from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split()) 


box = [[[0]*M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        box[h][n] = list(map(int, input().split()))

queue = deque()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 1:
                queue.append((z, x, y))

dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append((nz, nx, ny))

result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                exit(0)
            result = max(result, box[h][n][m])
print(result - 1)