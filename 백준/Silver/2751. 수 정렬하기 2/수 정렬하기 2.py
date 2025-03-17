import sys
N = int(sys.stdin.readline().strip())
A = [int(sys.stdin.readline().strip()) for _ in range(N)]

A.sort()

sys.stdout.write("\n".join(map(str, A))+"\n")