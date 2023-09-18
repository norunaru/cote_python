import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = [[0 for j in range(n + 1)]]
sumNum = [[0 for j in range(n + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    temp = [0]
    temp.extend(list(map(int, input().split())))
    numbers.append(temp)


for y in range(1, n + 1):
    for x in range(1, n + 1):
        sumNum[y][x] = (
            sumNum[y - 1][x] + sumNum[y][x - 1] - sumNum[y - 1][x - 1] + numbers[y][x]
        )

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = (
        sumNum[x2][y2]
        - sumNum[x2][y1 - 1]
        - sumNum[x1 - 1][y2]
        + sumNum[x1 - 1][y1 - 1]
    )
    print(result)
