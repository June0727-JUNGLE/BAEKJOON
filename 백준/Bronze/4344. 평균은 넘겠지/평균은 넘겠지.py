#평균은 넘겠지
C = int(input())
test_cases = []

for _ in range(C):
    data = list(map(int, input().split()))
    N = data[0] #학생수
    scores = data[1:]
    test_cases.append((N, scores))

for i in range(C):
    num_student = test_cases[i][0]
    scores = test_cases[i][1]
    
    avg = sum(scores) / num_student
    count =0
    for j in range(len(scores)):
        if test_cases[i][1][j] > avg:
            count+=1
    prtg = (count / num_student) * 100

    print(f'{prtg:.3f}%')