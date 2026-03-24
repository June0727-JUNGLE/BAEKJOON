Data = [list(map(int, input().split())) for i in range(9)]
max_value = 0
y_index = 0
x_index = 0
for y in range(len(Data)):
    for x in range(len(Data[y])):
        if Data[y][x]>max_value:
            max_value = Data[y][x]
            y_index = y
            x_index = x 


print(max_value)
print(y_index + 1, x_index + 1)

