import sys
input = sys.stdin.readline  

howmany, quizNo = map(int, input().split())
Data = list(map(int, input().split()))
preSum = [0] * (howmany + 1)
preSum[0] = 0
for i in range(1, howmany + 1):
    preSum[i] = preSum[i-1] + Data[i-1]

for _ in range(quizNo):
    start, end = map(int, input().split())
    print(preSum[end] - preSum[start-1])