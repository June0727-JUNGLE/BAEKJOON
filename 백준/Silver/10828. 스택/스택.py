import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.stk = []

    def push(self, x):
        self.stk.append(x)

    def pop(self):
        if self.empty():
            print(-1)
        else:
            print(self.stk.pop())

    def size(self):
        print(len(self.stk))

    def empty(self):
        return 1 if len(self.stk) == 0 else 0

    def top(self):
        if self.empty():
            print(-1)
        else:
            print(self.stk[-1])

stack = Stack()

n = int(input())
for _ in range(n):
    command = input().strip()

    if command.startswith("push"):
        _, x = command.split()
        stack.push(int(x))
    elif command == "pop":
        stack.pop()
    elif command == "size":
        stack.size()
    elif command == "empty":
        print(stack.empty())
    elif command == "top":
        stack.top()

        