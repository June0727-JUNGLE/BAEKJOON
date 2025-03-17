height = []
for _ in range(9):
    h = int(input())
    height.append(h)

total_sum = sum(height)

for i in range(8):
    for j in range(i+1, 9):
        if total_sum - height[i] - height[j] == 100:
            fake_1, fake_2 = height[i], height[j]
            break
    if len(height) == 7:
        break
height.remove(fake_1)
height.remove(fake_2)
height.sort()

for h in height:
    print(h)
