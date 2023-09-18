"""
숫자의 개수 N, 합을 구해야 하는 횟수 M

단순히 리스트 슬라이싱으로 구현하면 시간 초과 O(MN)
-> 자주 사용되는 정보는 미리 구해서 저장하고, 필요할 떄 꺼내서 사용한다. O(M+N)

입력되는 숫자들을 하나씩 순서대로 더하면서 결과 리스트를 만들어 놓고 시작, 끝 인덱스가 주어지면 사용한다.

"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sum_num = [0]

temp = 0
for i in numbers:
    temp += i
    sum_num.append(temp)

for i in range(m):
    start, end = map(int, input().split())
    print(sum_num[end] - sum_num[start - 1])
