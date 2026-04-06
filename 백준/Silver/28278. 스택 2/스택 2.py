import sys
input = sys.stdin.readline

N = int(input())
stack = []


def is_Empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def pop():
    if is_Empty():
        return -1
    else:
        return stack.pop()

def peek():
    if is_Empty():
        return -1
    else:
        return stack[-1]


for _ in range(N):
    order = list(map(int, input().split()))

    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        print(pop())
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        print(is_Empty())
    elif order[0] == 5:
        print(peek())
