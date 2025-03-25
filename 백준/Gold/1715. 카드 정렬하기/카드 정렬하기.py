import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)  # 최소 힙으로 변환
total = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    cost = a + b
    total += cost
    heapq.heappush(cards, cost)

print(total)