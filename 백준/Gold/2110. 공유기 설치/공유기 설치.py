import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort()

low = 1
high = house[-1] - house[0]
result = 0

def can_install(distance):
    count = 1
    last = house[0]

    for i in range(1, N):
        if house[i] - last >= distance:
            count += 1
            last = house[i]
    return count >= C
    
while low <= high:
    mid = (high+low)//2
    if can_install(mid):
        result = mid
        low = mid+1
    else: 
        high = mid-1

print(result)