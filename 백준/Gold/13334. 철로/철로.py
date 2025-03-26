import sys
import heapq
input = sys.stdin.readline

n = int(input())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    
    pos.append((x, y))
length = int(input())

pos.sort(key=lambda x: x[1])

heap = []
max_count = 0

for start, end in pos:
    if end - start > length:
        continue

    heapq.heappush(heap, start)

    while heap and heap[0] < end - length:
        heapq.heappop(heap)

    max_count = max(max_count, len(heap))

print(max_count)
