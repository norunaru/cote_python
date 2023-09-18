"""
체스판이 8*8 좌표평면이다. 특정 한 칸에 나이트가 있다.
나이트는 L자 형태로만 이동 가능하며 정원 밖으로는 나갈 수 없다.
1. 수평으로 2칸, 수직으로 1칸
2. 수직으로 2칸, 수평으로 1칸

행 위치 표현시 1~8로 표현하고, 열 위치 표현시 a~h로 표현

첫 줄에 좌표평면상 나이트 위치의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다 ex) a1
나이트가 이동할 수 있는 경우의 수를 출력하라.
"""

"""
내 코드

# 알파벳, 숫자의 합으로 이루어진 위치 입력받음
position = list(input())
# 알파벳을 숫자로 변환
x = int(ord(position[0]) - 96)
y = int(position[1])
print(x)
print(y)

# 갈 수 있는 경우의 수를 저장한 변수
count = 0

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(8):
    current_x = x
    current_y = y
    moved_x = current_x + dx[i]
    moved_y = current_y + dy[i]
    if 1 <= moved_x <= 8 and 1 <= moved_y <= 8:
        count += 1
print(count)

"""

# 요구사항대로 충실히 구현하면 되는 문제
# 8가지 경로를 확인하여 위치로 이동 가능한지 확인
# 리스트를 이용하여 8가지 방향에 대해 방향벡터 정의

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

# 나이트가 이동 가능한 8가지 방향 정의
steps = [
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
    (2, -1),
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
]

# 8가지 방향에 대해 각 위치로 이동 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
