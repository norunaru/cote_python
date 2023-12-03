T = 10
for _ in range(T):
    tc = int(input())

    # 문자열 담은 보드 생성
    board = []
    for i in range(100):
        board.append(list(input()))

    result = 0

    # 길이를 1부터 100까지 확인
    for length in range(1, 101):
        # 각 좌표에 대해 완전탐색
        for a in range(100):
            for b in range(100 - length + 1):
                A = []  # 가로 문자열
                B = []  # 세로 문자열
                for x in range(length):
                    A.append(board[a][b + x])
                    B.append(board[b + x][a])
                A = "".join(A)
                B = "".join(B)
                if A == A[::-1] or B == B[::-1]:
                    result = length
                    break
            if A == A[::-1] or B == B[::-1]:
                result = length
                break

    print(f"#{tc} {result}")


# 그 좌표부터 시작하는 문자열이 펠린드롬이면 다른 좌표들 살펴볼 필요 없이 다음 길이로 넘어간다.
