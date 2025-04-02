import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((cost, v))

start, target = map(int, input().split())

def dijkstra(start, target):
    distance = [float("inf")] * (N+1)
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        current_cost, u = heapq.heappop(hq)
        if distance[u] < current_cost:
            continue
        for next_cost, v in graph[u]:
            new_cost = current_cost + next_cost
            if new_cost < distance[v]:
                distance[v] = new_cost
                heapq.heappush(hq, (new_cost, v))
    return distance[target]

print(dijkstra(start, target))
