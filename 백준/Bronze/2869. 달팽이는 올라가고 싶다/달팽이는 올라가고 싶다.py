import math
A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:
    days = math.ceil((V-A)/((A-B)))+1
    print(days)