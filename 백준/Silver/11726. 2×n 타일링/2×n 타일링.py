n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a, b = 1, 2  # a = dp[1], b = dp[2]
    for _ in range(3, n + 1):
        a, b = b, (a + b) % 10007  # b = dp[i-1], a = dp[i-2]
    print(b)
