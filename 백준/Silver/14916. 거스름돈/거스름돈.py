import sys
input = sys.stdin.readline
INF = float('inf')
N = int(input())
dp = [INF] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    if i >= 2 and dp[i-2] != INF:
        dp[i] = min(dp[i], dp[i-2]+1)
    if i >= 5 and dp[i-5] != INF:
        dp[i] = min(dp[i], dp[i-5]+1)

print(dp[N] if dp[N] != INF else -1)