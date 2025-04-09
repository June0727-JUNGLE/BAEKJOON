import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))  # 1-indexed
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    target = int(input())

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = cost[i]

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[now] + cost[nxt])
            if indegree[nxt] == 0:
                queue.append(nxt)

    print(dp[target])