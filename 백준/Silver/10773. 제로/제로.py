import sys
input = sys.stdin.readline

K = int(input())
total = 0
stack = [] * K

for _ in range(K):
    N = int(input())
    if N != 0:
        stack.append(N)
        total += N
    else:
        total -= stack.pop()

print(total)
