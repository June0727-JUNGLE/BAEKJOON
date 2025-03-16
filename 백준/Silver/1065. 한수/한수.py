N = int(input())

if N < 100:
    print(N)
else:
    count = 99
    for i in range(100, N+1):
        j = str(i)
        if int(j[0]) - int(j[1]) == int(j[1]) - int(j[2]):
            count+=1
    print(count)