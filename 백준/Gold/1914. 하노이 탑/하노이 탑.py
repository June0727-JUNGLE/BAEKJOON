import sys

def hanoi_S(n,a,b,c,result):
    if n == 1:
        result.append(f"{a} {c}\n")
        return
    hanoi_S(n-1,a,c,b,result)
    result.append(f"{a} {c}\n")
    hanoi_S(n-1,b,a,c,result)
    
n = int(sys.stdin.readline().strip())
print(2**n-1)
if n <= 20:
    result =[]    
    hanoi_S(n,1,2,3, result)
    sys.stdout.write("".join(result))