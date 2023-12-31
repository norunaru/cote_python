"""
정수 X가 주어졌을 때 X에 사용 가능한 연산은 4가지이다.
1. X가 5로 나누어 떨어지면 5로 나눈다.
2. X가 3으로 나누어 떨어지면 3으로 나눈다.
3. X가 2로 나누어 떨어지면 2로 나눈다.
4. X에서 1을 뺸다.

정수 X가 주어졌을 때 연산 4개를 적절히 사용하여 값을 1로 만들고자 한다.
연산 사용하는 횟수의 최솟값을 출력하라.
예를 들어 정수가 26이면 3번의 연산이 최솟값이다.
26 -> 25 -> 5 -> 1

첫째 줄에 정수 X가 주어진다.
첫째 줄에 연산의 최소 횟수를 출력하라
26
답 : 3
"""
x = int(input())

# 앞서 계산한 결과를 저장하기 위한 DP테이블 초기화
# 0번 인덱스는 사용x, 1번 인덱스(값 x가 1이면 연산 횟수 0)도 사용 x
d = [0] * 30001

# DP 진행 - 바텀업
# 0,1인덱스는 사용 안하므로 빼고, 2부터 입력으로 들어온 x까지의 최적값을 배열에 저장한다.
for i in range(2, x + 1):
    # 현재 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    # 2로 나눈 위치에서의 최적해에 1을 더한 값과 비교한다.
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 3로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
