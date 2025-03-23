import sys

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 0
def cut_rect(x, y, size):
    global white, blue

    total = 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            total += grid[i][j]

    if total == 0:
        white+=1
    elif total == size*size:
        blue+=1
    else:
        half = size //2
        cut_rect(x,y, half)
        cut_rect(x,y+half,half)
        cut_rect(x+half,y,half)
        cut_rect(x+half,y+half,half)

cut_rect(0,0,n)
print(white)
print(blue)