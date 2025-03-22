import sys
import bisect
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

def is_possible(length):
    dp = []
    for num in N_list:
        idx = bisect.bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
        if len(dp) >= length:
            return True
    return False

low = 1
high = N
answer = 1  # 최소 LIS는 1 이상이므로 초기값 1

while low <= high:
    mid = (low + high) // 2
    if is_possible(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
