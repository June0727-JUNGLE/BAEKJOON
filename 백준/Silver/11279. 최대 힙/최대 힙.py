import heapq
import sys
input = sys.stdin.readline
n = int(input())

max_pq = []

for _ in range(n):
    x= int(input().strip())
    if x == 0:
        if len(max_pq) == 0:
            print(0)
        else:
            print(-heapq.heappop(max_pq))
    else: 
        heapq.heappush(max_pq, -x)
        