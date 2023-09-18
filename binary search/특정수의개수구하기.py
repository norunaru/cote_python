"""
N개의 원소를 포함하는 소열이 오름차순으로 정렬되어 있다. 이때 이 수열에서 x가 등장하는 횟수를 계산하라.
예를 들어 수열 {1,1,2,2,2,2,3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다.
단 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하라

첫째 줄에 N, x가 정수 형태로 입력된다.
둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다.
출력 조건 : 값이 x인 원소의 개수를 출력한다. 단 값이 x인 원소가 하나도 없다면 -1 출력.
"""

from bisect import bisect_right, bisect_left


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x,x]범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
