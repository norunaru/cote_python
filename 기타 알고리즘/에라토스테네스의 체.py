import math

n = 1000
# 2~1000 범위의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2~n의 제곱근까지 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:  # i가 소수인경우
        # i를 제외한 모든 i의 배수 지우기
        j = 2  # j는 배수 변수
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")
"""
시간 복잡도는 O(NloglogN)

"""
