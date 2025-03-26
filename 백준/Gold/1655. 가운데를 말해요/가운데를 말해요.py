import sys
import heapq
input = sys.stdin.readline

n = int(input())
left = []
right = []
for _ in range(n):
    x = int(input().strip())
    heapq.heappush(left, -x)
    if right and -left[0] > right[0]:
        heapq.heappush(right, -heapq.heappop(left))
    if len(left) > len(right)+1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right)>len(left):
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])