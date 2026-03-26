#import sys
#input = sys.stdin.readline

T = int(input())

dy = [0, 1, 0, -1]     #우, 하, 좌, 상 순으로
dx = [1, 0, -1, 0]

def is_safe(y, x):
    return 0 <= y < N and 0 <= x < N

for i in range(T):
    N = int(input())
    cnt = 1
    Data = [[0] * N for _ in range(N)]
    y, x = 0, 0
    Data[y][x] = cnt
    while cnt < N * N:
        for dir in range(4):
            newY = y + dy[dir]
            newX = x + dx[dir]
            while is_safe(newY, newX) and Data[newY][newX] == 0:
                cnt += 1
                Data[newY][newX] = cnt
                y, x = newY, newX
                newY = y + dy[dir]
                newX = x + dx[dir]
    print(f'#{i+1}')
    for row in Data:
        print(*row)

                

