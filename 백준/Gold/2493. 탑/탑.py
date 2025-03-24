import sys
from collections import deque

n = int(sys.stdin.readline())
Tower = list(map(int, sys.stdin.readline().split()))
result = []
stack = []

for i in range(n):
    curr_tower = Tower[i]

    while stack and stack[-1][1] < curr_tower:
        stack.pop()

    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)
    stack.append((i, curr_tower))
    
   
print(' '.join(map(str, result)))