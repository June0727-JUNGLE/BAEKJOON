n = int(input())
dp = [0] * (n + 2)  # n == 1일 경우 대비
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
