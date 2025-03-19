def sol(k):
    global n, cnt

    if k == n:
        cnt += 1
        return
    for i in range(n):
        if not used_c[i] and not used_xy[k+i] and not used_yx[(n-1)+k-i]:
            used_c[i] = True
            used_xy[k+i] = True
            used_yx[(n-1)+k-i] = True
            sol(k+1)
            used_c[i] = False
            used_xy[k+i] = False
            used_yx[(n-1)+k-i] = False

n = int(input())
maps = [[0]*n for _ in range(n)]
used_c = [False]*n
used_xy = [False]*(2*(n-1)+1)
used_yx = [False]*(2*(n-1)+1)

cnt = 0

sol(0)
print(cnt)