T = int(input())

for _ in range(T):
    R, S = input().split()  
    R = int(R)
    P = ""
    for char in S:
        P += char * R
    print(P)
