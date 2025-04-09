import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[-1] * N for _ in range(1 << N)]

def tsp(visited, current, start):
    if visited == (1 << N) - 1:
        return W[current][start] if W[current][start] > 0 else INF

    if dp[visited][current] != -1:
        return dp[visited][current]

    min_cost = INF
    for next in range(N):
        if visited & (1 << next): continue
        if W[current][next] == 0: continue
        next_visited = visited | (1 << next)
        cost = tsp(next_visited, next, start) + W[current][next]
        min_cost = min(min_cost, cost)

    dp[visited][current] = min_cost
    return min_cost

# 시작 도시를 0부터 N-1까지 모두 시도
answer = INF
for start in range(N):
    dp = [[-1] * N for _ in range(1 << N)]  # 각 시작점마다 초기화
    answer = min(answer, tsp(1 << start, start, start))

print(answer)

