"""
각 자리가 숫자 0~9로 이루어진 문자열 S가 주어졌을 떄, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 
숫자 사이에 +나 * 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라. 
단 +보다 *를 먼저 계산하는 일반적 방식과 달리 모든 연산은 왼쪽부터 순서대로 이루어진다. 
만들어질 수 있는 가장 큰 수는 20억 이하의 정수가 되도록 입력이 주어진다
"""


"""
내 코드
S = list(input())
numbers = 0

for i in S:
    i = int(i)
    if(i == 0 or i == 1):
        numbers += i
    else:
        numbers *= i
print(numbers)
"""

"""
대부분의 경우 + 보다 *가 값이 더 커진다.
다만 숫자가 0,1인 경우 +가 효과적]
따라수 연산 수행시 두 수 중에 하나라도 1 이하인 경우 더하기, 두 수가 모두 2 이상이면 곱하는 것이 정답
"""

data = input()

# 첫 번쨰 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수중에 하나라도 0,1인 경우 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result += num
print(result)
