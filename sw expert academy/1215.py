"""
len = 4 -> 

(0,8-len+1) 가로 세로 제한
0~4를 시작 인덱스 (i,i+4)

0 1 2 3 4 5 6 7 
1
2
3
4
5
6
7


"""

for tc in range(1, 11):
    length = int(input())
    count = 0

    # 보드 생성
    board = []
    for _ in range(8):
        board.append(list(input()))

    for a in range(0, 8):
        for b in range(0, 8 - length + 1):  # (0,5) 0~4
            A = []  # 가로 문자열
            B = []  # 세로 문자열
            for x in range(length):  # 0,1,2,3
                A.append(board[a][b + x])
                B.append(board[b + x][a])
            A = "".join(A)
            B = "".join(B)
            # print(f"a : {a} b : {b} A : {A} B : {B}")
            if A == A[::-1]:
                # print(A)
                count += 1
            if B == B[::-1]:
                # print(B)
                count += 1
    print(f"#{tc} {count}")
