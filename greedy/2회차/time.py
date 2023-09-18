position = list(input())

x = ord(position[0]) - 96
y = int(position[1])
print(x, y)
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

count = 0

for i in range(8):
    if x + dx[i] < 1 or x + dx[i] > 8 or y + dy[i] < 1 or y + dy[i] > 8:
        continue
    else:
        print(x + dx[i], y + dy[i])
        count += 1
print(count)
