n, m = map(int, input().split())

inputChess = []
for i in range(n):
    inputChess.append(list(input()))
repair = []

for start_Y in range(n - 7):
    for start_X in range(m - 7):
        first_W = 0  # 첫 칸이 흰색인 체스판
        first_B = 0  # 첫 칸이 검은색인 체스판

        # 입력한 보드의 일부분을 8*8 체스판 모양으로 자르고 각 칸에 대하여 처리
        for cut_Y in range(start_Y, start_Y + 8):
            for cut_X in range(start_X, start_X + 8):
                # 행과 열의 인덱스 합이 짝수인 경우 같은 색을 가지게 된다.
                # 행 + 열 = 짝
                if (cut_Y + cut_X) % 2 == 0:
                    # 첫 칸이 흰색인 체스판의 경우 행+열=짝 칸의 색들이 흰색이 아니면 +1
                    if inputChess[cut_Y][cut_X] != "W":
                        first_W += 1
                    # 첫 칸이 검은색인 체스판의 경우 행+열=짝 칸의 색들이 검은색이 아니면 +1
                    if inputChess[cut_Y][cut_X] != "B":
                        first_B += 1
                # 행 + 열 = 홀
                elif (cut_Y + cut_X) % 2 == 1:
                    if inputChess[cut_Y][cut_X] != "B":
                        first_W += 1
                    if inputChess[cut_Y][cut_X] != "W":
                        first_B += 1
        repair.append(first_W)
        repair.append(first_B)
print(min(repair))
