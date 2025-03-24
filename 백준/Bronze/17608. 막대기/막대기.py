import sys
from collections import deque

n = int(sys.stdin.readline())
log_watch = deque()
for i in range(n):
    a = int(sys.stdin.readline().strip())

    if i == 0:
        log_watch.append(a)
    else:
        while log_watch and log_watch[-1] <= a:
            log_watch.pop()
        log_watch.append(a)

print(len(log_watch))
