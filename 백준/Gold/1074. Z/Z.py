def Rect(N, r, c):
    if N == 0:
        return 0
    half = 2**(N-1)
    if r < half and c < half:
        return Rect(N-1, r, c) 
    elif r < half and c >= half:
        return Rect(N-1, r, c-half) + half*half
    elif r >= half and c < half:
        return Rect(N-1, r-half, c) + half*half*2
    else:
        return Rect(N-1, r-half, c-half) + half*half*3
    
N, r, c = map(int, input().split())

print(Rect(N, r, c))