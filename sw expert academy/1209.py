T = 10


for test_case in range(1, T + 1):
    tc = int(input())
    board = []

    # 100 * 100 보드 생성
    for i in range(100):
        inputs = list(map(int, input().split()))  # 길이 10000(0~9999)
        board.append(inputs)

    board.append([0] * 100)  # 가로 100 (0~99), 세로 101 (0~100, 100인덱스는 빈칸)
    print(len(board[100]))

    # 가로 합
    for row in range(100):
        sumRow = sum(board[row])
        board[row].append(sumRow)  # 이 반복문 끝나면 가로 101, 마지막에 그 행의 sum
    # 세로 합
    for col in range(100):
        sumCol = 0
        for row in range(100):
            sumCol += board[row][col]
        board[100][col] = sumCol
    # 대각선 합
    sumRight = 0
    sumLeft = 0
    for x in range(100):
        sumRight += board[x][x]
    for a in range(100, 0):
        for b in range(0, 100):
            sumLeft += board[a][b]

    result = board[100]

    for i in range(100):
        result.append(board[i][100])
    result.append(sumRight)
    result.append(sumLeft)

    print(f"#{test_case} {max(result)}")
