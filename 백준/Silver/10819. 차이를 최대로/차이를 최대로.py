n = int(input())
N = list(map(int, input().split()))

def sum_arr(a:list)->int:
    return sum(abs(a[i]-a[i+1]) for i in range(len(a)-1)) 


def find_all_arr(a:list)->list:
    if len(a) == 1:
        return [a]
    
    result = [] 
    for i in range(len(a)):
        current = a[i]
        remain = a[:i] + a[i+1:]
        for j in find_all_arr(remain):
            result.append([current]+j)
    return result
    
permutation = find_all_arr(N)

max_diff_sum = max(sum_arr(k) for k in permutation)

print(max_diff_sum)