"""
위가 N, 아래가 S극, 빨간 자성체는 아래(S)쪽으로 붙고, 파란 자성체는 위(N)쪽으로 붙는다.

자기장이 흐를 때 막아주는 자성체가 없으면 끌려가다 테이블 아래로 떨어진다. 

빨빨파 -> 1개 교착상태, 빨파빨파 -> 2개 
(같은 색의 덩어리는 하나로 취급 빨빨파 -> 빨파)


1은 N극성질 자성체, 2는 S극 성질 자성체, 테이블 위가 1, 아래가 2

1자성체는 2쪽으로, 2자성체는 1쪽으로 이동
"""
T = 10

for tc in range(1, 11):  # 테스트케이스 10번
    side = int(input())

    count = 0

    # 보드 생성
    board = []
    for i in range(100):
        board.append(list(map(int, input().split())))

    # 체크
    for col in range(100):
        temp = []
        for row in range(100):
            if board[row][col] != 0:
                temp.append(board[row][col])
        # 여기까지 하면 한 열에 대해 1,2만 남음

        # 맨 앞 자성체가 1이 아니면 계속 삭제
        while temp[0] != 1:
            temp.pop(0)
        # 마지막 자성체가 2가 아니면 계속 삭제
        while temp[-1] != 2:
            temp.pop()
        print(temp)
        # temp의 개수 카운트
        tempCount = 0
        length = len(temp)
        for current in range(length - 1):
            if str(temp[current]) + str(temp[current + 1]) == "12":
                count += 1
    print(f"#{tc} {count}")
