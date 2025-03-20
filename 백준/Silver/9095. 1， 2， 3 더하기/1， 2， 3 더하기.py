T = int(input())
t= []
for _ in range(T):
    t.append(int(input()))

def count_ways(n, current=0):
    # 현재 누적합이 목표에 도달하면 하나의 경우로 셈
    if current == n:
        return 1
    # 현재 누적합이 목표를 초과하면 유효한 경우가 아님
    if current > n:
        return 0

    ways = 0
    # 1, 2, 3을 각각 더해가며 경우의 수를 누적합니다.
    for num in [1, 2, 3]:
        ways += count_ways(n, current + num)
    return ways

for i in range(T):
    print(count_ways(t[i]))