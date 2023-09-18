"""
n * m 크기의 금광이 있다. 금광은 1 * 1 크기의 칸으로 나누어지며 각 칸은 랜덤한 양의 금이 들어있다.
채굴자는 첫 번쨰 열부터 금을 캐기 시작한다. 맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다.
이후 m-1 번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 최대 금의 크기를 출력하는 프로그램을 작성하라.

첫째 줄에 테스트 케이스 T가 입력된다.
매 테스트 케이스 첫줄에 n,m이 공백으로 구분되어 입력된다 (1 <= n, m <= 20)
둘째 줄에 n*m 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다. (1 <= 각 위치의 금의 양 <= 100)

테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다.
각 테스트 케이스는 줄바꿈을 이용해 구분합니다.
입력 : 
2
3 4 
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

출력 : 
19
16
"""

for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # DP 위한 2차원 테이블 초기화
    dp = []
    index = 0
    # 금광 정보가 한줄로 입력되므로 m단위로 슬라이싱하여 dp 테이블에 넣어준다.
    for i in range(n):
        dp.append(array[index : index + m])
        index += m
    # DP 진행
    # 열 기준으로 각 데이터 확인하며 데이터 갱신 - 각 열마다 각 행 확인
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위, 아래에서 오는 경우는 인덱스가 범위 벗어나는지 확인 및 처리 필요.
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
