"""
4 5
00110
00011
11111
00000
"""
# 내 코드 - 정답
N, M = map(int, input().split())

ice = []
count = 0

for i in range(N):
    ice.append(list(input()))

for i in range(N):
    for j in range(M):
        ice[i][j] = int(ice[i][j])

for i in range(N):
    print(ice[i])

# 상하좌우
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def dfs(i, j):
    ice[i][j] = 1
    for move in moves:
        nx = j + move[1]
        ny = i + move[0]
        if ny < 0 or ny > N - 1 or nx < 0 or nx > M - 1:
            continue
        elif ice[ny][nx] == 0:
            dfs(ny, nx)


for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            count += 1
            dfs(i, j)


print(count)
