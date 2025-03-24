import sys
from collections import deque
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.que = deque()

    def empty(self):
        if len(self.que) == 0:
            return 1
        else:
            return 0

    def push(self, x):
        self.que.append(x)

    def pop(self):
        if self.empty():
            print(-1)
        else:
            print(self.que.popleft())

    def size(self):
        print(len(self.que))

    def front(self):
        if self.empty():
            print(-1)
        else:
            print(self.que[0])
    
    def back(self):
        if self.empty():
            print(-1)
        else:
            print(self.que[-1])

queue = Queue()

n = int(input())
for _ in range(n):
    command = input().strip()

    if command.startswith("push"):
        _, x = command.split()
        queue.push(int(x))
    elif command == "pop":
        queue.pop()
    elif command == "size":
        queue.size()
    elif command == "empty":
        print(queue.empty())
    elif command == "front":
        queue.front()
    elif command == "back":
        queue.back()