n = int(input())
MOD = 1_000_000_000

dp = [[0] * 10 for _ in range(n + 1)]

# 1자리 수 초기화
for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]
        if j + 1 <= 9:
            dp[i][j] += dp[i - 1][j + 1]
        dp[i][j] %= MOD

print(sum(dp[n]) % MOD)
