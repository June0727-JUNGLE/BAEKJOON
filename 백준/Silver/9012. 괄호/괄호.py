import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    stack_vps = deque()
    x = sys.stdin.readline().strip()
    is_vps = True
    for j in range(len(x)):
        if x[j] == '(':
            stack_vps.append(1)
        else:
            if not stack_vps:
                is_vps = False
                break
            stack_vps.pop()
    if stack_vps:
        is_vps = False
    print("YES" if is_vps else "NO")