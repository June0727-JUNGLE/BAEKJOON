#골드바흐 추측
n = int(input()) #입력받을 개수
inputs = [] #입력받은 수 저장

"""소수인지 판단"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

#개수만큼 입력을 받아서 리스트에 저장    
for _ in range(n):
    value = int(input())
    inputs.append(value)


for k in inputs:
    l = k // 2  
    for a in range(l, 1, -1):  
        b = k - a
        if is_prime(a) and is_prime(b) == True:
            print(a, b)    
            break 