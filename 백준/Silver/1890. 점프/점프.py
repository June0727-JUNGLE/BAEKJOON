import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]  # -1: 아직 계산하지 않은 상태

def dfs(x, y):
    if x >= N or y >= N:
        return 0
    if x == N - 1 and y == N - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0  # 초기화
    jump = board[x][y]
    if jump == 0:
        return 0

    dp[x][y] += dfs(x + jump, y)  # 아래로 점프
    dp[x][y] += dfs(x, y + jump)  # 오른쪽으로 점프

    return dp[x][y]

print(dfs(0, 0))