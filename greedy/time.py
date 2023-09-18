"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
모든 경우의 수를 구하는 프로그램을 작성하라. 예를 들어 1을 입력시 다음은 3이 하나라도 포함되어있으므로 세어야 하는 시각이다.
- 00시 00분 03초
- 00시 13분 30초
다음은 3이 포함되지 않으므로 세면 안되는 시각
- 00시 02분 55초
- 01시 27분 45초

첫쨰 줄에 N 입력됨 (0~23)
"""
"""
내 코드

N = int(input())
count = 0
hour = 0
minute = 0
second = 0

for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            time = str(hour) + str(minute) + str(second)
            if "3" in time:
                count += 1
print(count)
"""

"""
가능한 모든 시각의 경우를 모두 세서 풀 수 있는 문제 (완전 탐색 문제 - brute forcing)
하루는 86400초 -> 파이썬은 1초에 약 2천만 연산 -> 충분히 시간 내 해결 가능
"""

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각안에 '3'이 포함되면 카운트 증가
            if "3" in str(i) + str(j) + str(k):
                count += 1
print(count)
