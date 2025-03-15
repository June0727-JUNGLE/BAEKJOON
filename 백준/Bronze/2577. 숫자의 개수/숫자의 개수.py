from collections import Counter
a = int(input())
b = int(input())
c = int(input())
n = a*b*c

def count_digits(n):
    k = str(n)
    counter = Counter(k)

    for i in range(0,10):
        print(f'{counter[str(i)]}')

count_digits(n)