x, y = map(int, input().split())
n = int(input())
X = [0,x]
Y = [0,y]

rect = []
for _ in range(n):
    direct, pos = map(int, input().split())
    if direct == 0:
        Y.append(pos)
    else:
        X.append(pos)

X.sort()
Y.sort()

length_X = []
length_Y = []
for i in range(len(X)-1):
    length_X.append(X[i+1] - X[i])
for i in range(len(Y)-1):
    length_Y.append(Y[i+1] - Y[i])

max_x = max(length_X)
max_y = max(length_Y)

area = max_x * max_y
print(area)