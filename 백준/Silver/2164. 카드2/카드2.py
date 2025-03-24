import sys
from collections import deque

n = int(sys.stdin.readline())
Card = deque(range(1,n+1))

while len(Card)>1:
    Card.popleft()
    Card.append(Card.popleft())

print(Card[0])