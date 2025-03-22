import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
M_List = list(map(int, input().split()))
M_List.sort()

animals = [tuple(map(int, input().split())) for _ in range(N)]

count = 0

def search_animal(x, y):
    low = 0
    high = M - 1
    while low <= high:
        mid = (low+high) // 2
        gun_x = M_List[mid]
        distance = abs(gun_x - x) + y
        if distance <= L:
            return True
        elif gun_x < x:
            low = mid + 1
        else:
            high = mid -1
    return False

for x, y in animals:
    if y > L:
        continue
    if search_animal(x, y):
        count += 1

print(count)
