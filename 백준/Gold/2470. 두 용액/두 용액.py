import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
inf = float('inf')
location = (0, 0)
for i in range(N-1):
    target = N_list[i]
    low = i+1
    high = N-1
    while low <= high:
        mid = (low+high) // 2
        total = target + N_list[mid]
        
        if abs(total) < inf:
            inf = abs(total)
            location = (N_list[i], N_list[mid])
        
        if total == 0:
            break
        elif total > 0:
            high = mid - 1
        else:
            low = mid + 1
    
print(*location)