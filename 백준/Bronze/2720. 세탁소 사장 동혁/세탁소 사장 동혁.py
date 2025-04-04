import sys
input = sys.stdin.readline

t = int(input())
test_list = [int(input())for _ in range(t)]
coins = [25,10,5,1]

for cost in test_list:
    res = []
    for coin in coins:
        count = cost//coin
        cost %=coin
        res.append(count)
    print(*res)