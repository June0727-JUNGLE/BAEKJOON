import sys
input = sys.stdin.readline

n = int(input())
dims = []

for i in range(n):
    r, c = map(int, input().split())
    if i == 0:
        dims.append(r)
    dims.append(c)

dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1):  # 부분 수열 길이
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n - 1])
