import sys
input = sys.stdin.readline

N = int(input())

def max_sum(N):
    for y in range(N//5, -1, -1):
        remain = N - 5*y
        if remain % 3 == 0:
            x = remain // 3
            return x+y
    return -1
print(max_sum(N))