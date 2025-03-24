import sys

def largest_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[stack[-1]]>heights[i]:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] -1
            area = h * width
            max_area = max(max_area, area)
        stack.append(i)
    return max_area

while True:
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == 0:
        break
    n, heights = line[0], line[1:]
    print(largest_area(heights))
 
            