import sys
import heapq
input = sys.stdin.readline
N, M, X = map(int, input().split())

graph = [[]for _ in range(N+1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v,t))

def dijkstra(graph, start, target):
    distance = [float('inf')] * (len(graph))
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        current_cost, current_node = heapq.heappop(hq)
        if current_cost > distance[current_node]:
            continue
        for next_node, cost in graph[current_node]:
            new_cost = current_cost + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))
    return distance[target]
res = [0] * (N+1)
for i in range(1, N+1):
    res[i] += dijkstra(graph, i, X)
    res[i] += dijkstra(graph, X, i)

print(max(res))