import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    
    apt = [[0]*15 for _ in range(k+1)]
    #조건
    for i in range(1,n+1):
        apt[0][i] = i

    #점화식
    for i in range(1, k+1):
        for j in range(1, n+1):
            apt[i][j] = apt[i][j-1] + apt[i-1][j]

    print(apt[k][n])
