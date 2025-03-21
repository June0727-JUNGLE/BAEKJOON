import sys
input = sys.stdin.readline       

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

low = 0
high = max(N_list)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = 0

    for tree in N_list:
        if tree > mid:
            total += tree-mid

    if total >= M:
        result = mid
        low = mid+1
    
    else:
        high = mid-1

print(result)