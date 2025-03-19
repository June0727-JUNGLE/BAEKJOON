import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_rain = max(map(max, graph)) #높이 중에 제일 높은 값을 저장

dx = [0,0,-1,1] #오른쪽으로 한칸, 왼쪽으로 한칸, 위로 한칸, 아래로 한칸
dy = [1,-1,0,0]
def bfs(i,j): #안전영역의 개수 체크, 인접한 영역 체크
    global count
    q = deque()
    q.append((i,j))
    sink[i][j] = True
    count+=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny  = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>= N:
                continue
            if sink[nx][ny] == False:
                sink[nx][ny] = True
                q.append((nx,ny))
count_list = []
for rain in range(max_rain): #비의 양 조절, max_rain보다 1이 작을 때까지 반복
    count = 0 #비 양이 바뀔 때마다 초기화 
    sink = [[False for _ in range(N)] for i in range(N)] #물에 잠긴 부분을 초기화
    for i in range(N): #graph[i][j]에 대해 잠긴 부분을 표시
        for j in range(N):
            if graph[i][j]<=rain:
                sink[i][j]=True #잠긴 부분을 True로 표시
    for i in range(N):
        for j in range(N):
            if sink[i][j] == False: #안잠긴 부분에 대해서
                bfs(i,j)
    count_list.append(count) #모두 체크했으면 안전영역의 개수를 저장

print(max(count_list))   
