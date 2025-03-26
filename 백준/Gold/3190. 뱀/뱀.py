import sys
from collections import deque
input = sys.stdin.readline

#N*N의 보드 생성
N = int(input())
board = [[0]*N for _ in range(N)]

#사과의 위치정보를 보드에 1로 표시
K = int(input())
apple = []
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
change_direction = {}
for _ in range(L):
    t, a = input().split()
    change_direction[int(t)] = a

dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction = 0

snake = deque()
snake.append((0,0))
time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not (0<=nx<N and 0<=ny<N):
        break
    if (nx, ny) in snake:
        break

    if board[nx][ny] == 1:
        board[nx][ny] = 0
        snake.append((nx, ny))
    else:
        snake.append((nx, ny))
        snake.popleft()

    x, y = nx, ny

    if time in change_direction:
        if change_direction[time] == "L":
            direction = (direction-1)%4
        elif change_direction[time] == "D":
            direction = (direction+1)%4

print(time)