import sys
import heapq
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dijkstra(graph):
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    hq = [(0, 0, 0)]

    while hq:
        count, cx, cy = heapq.heappop(hq)
        if cx == N-1 and cy == N-1:
            return count
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0<= ny < N:
                new_cnt = count +(1 if graph[nx][ny] == 0 else 0)
                if new_cnt < dist[nx][ny]:
                    dist[nx][ny] = new_cnt
                    heapq.heappush(hq, (new_cnt, nx, ny))
print(dijkstra(graph))