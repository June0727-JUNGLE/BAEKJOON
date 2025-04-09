import sys
input = sys.stdin.readline

N, K = map(int, input().split())
obj = list(map(int, input().split()))
multitap = []
count = 0

for i in range(K):
    now = obj[i]

    if now in multitap:
        continue

    if len(multitap) < N:
        multitap.append(now)
        continue

    latest_index = -1
    target = 0
    for plug in multitap:
        try:
            idx = obj[i+1:].index(plug)
        except ValueError:
            idx = float('inf')
        if idx > latest_index:
            latest_index = idx
            target = plug

    multitap.remove(target)
    multitap.append(now)
    count+=1

print(count)