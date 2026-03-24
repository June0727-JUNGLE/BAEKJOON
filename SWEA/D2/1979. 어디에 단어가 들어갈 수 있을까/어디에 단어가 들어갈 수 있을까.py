#import sys
#sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    Data = [list(map(int, input().split()))for i in range(N)]
    count = 0
    for y in range(N):
        cnt = 0
        for x in range(N):
            if Data[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    count += 1
                cnt = 0
        if cnt == K:
            count += 1

    for x in range(N):
        cnt = 0
        for y in range(N):
            if Data[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    count += 1
                cnt = 0
        if cnt == K:
            count += 1
    print(f'#{i+1} {count}')

            