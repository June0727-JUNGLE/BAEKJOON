#팩토리얼 계산
def fact(n):
    if n<1:
        return 1 #기저조건
    return n * fact(n-1)

n = int(input())
print(fact(n))