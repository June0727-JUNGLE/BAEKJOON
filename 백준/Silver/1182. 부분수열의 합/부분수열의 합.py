N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = []

def solve(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1

    for i in range(start, N):
        ans.append(num[i])
        solve(i+1)
        ans.pop() #리스트에서 마지막 요소를 제거

solve(0)
print(cnt)
