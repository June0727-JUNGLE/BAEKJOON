N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
used = [False] * (N)

def travel_path(matrix, n, current, current_cost, start, path_sums):
    """
    matrix: 행렬
    n: 현재까지 방문한 도시 수
    current: 현재 방문한 도시(인덱스)
    current_cost: 현재까지 누적된 비용
    start: 시작도시
    path_sums: 완성된 경로의 비용을 저장하는 리스트
    """
    if n == N:
        if matrix[current][start] != 0:
            path_sums.append(current_cost+matrix[current][start])
        return

    for next_city in range(N):
            if not used[next_city] and matrix[current][next_city] != 0:
                used[next_city] = True
                travel_path(matrix, n+1, next_city, current_cost + matrix[current][next_city], start, path_sums)
                used[next_city] = False
path_sums = []
for i in range(N):
    used[i] = True
    travel_path(matrix, 1, i, 0, i, path_sums)
    used[i] = False

print(min(path_sums))
