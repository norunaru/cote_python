"""
M*N 크기 보드 -> K*K크기로 자른다
맨 위가 흰색, 검은색 2경우

다시 칠해야 하는 정사각형 최소 개수 구하는 프로그램
"""
# import sys

# input = sys.stdin.readline

n, m, k = map(int, input().split())

board = []

for i in range(n):
    board.append(list(input()))
print(board)

whiteChess = [[0 for j in range(m)] for i in range(n)]
blackChess = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) // 2 == 0 and board[i][j] != "W":
            whiteChess += 1
