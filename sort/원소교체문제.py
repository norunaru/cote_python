"""
두 개의 배열 A,B를 가진다. 두 배열은 N개의 원소로 구성되어 있고, 원소는 모두 자연수이다.
최대 K번 바꿔치기 연산 수행 가능, 바꿔치기는 A의 원소 하나와 B의 원소 하나를 골라서 두 원소를 바꾸는 것.
최종 목표는 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
N,K, 그리고 배열 A,B의 정보가 주어질 때 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 
배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하라.

첫번쨰 줄에 N,K가 공백을 기준으로 구분되어 입력된다.
두 번째 줄에 A의 원소들이 공백을 기준으로 구분되어 입력된다.
세 번째 줄에 B의 원소들이 공백을 기준으로 구분되어 입력된다.
최대 K번의 바꿔치기 연산 수행시 A의 원소들의 합의 최댓값을 출력한다
5 3
1 2 5 4 3 
5 5 6 6 5

출력 : 26
"""

"""

import time

start_time = time.time()

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print("초기 A,B")
print(A)
print(B)


for i in range(K):
    A = sorted(A)
    B = sorted(B)
    A_min = A[0]
    B_max = B[len(B) - 1]
    A[0] = B_max
    B[len(B) - 1] = A_min
    print("{}번 스왑 결과 : ".format(i + 1))
    print(A)
    print(B)
print(sum(A))


end_time = time.time()
print(end_time - start_time)
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # A의 원소가 B보다 작으면 교체
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:  # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
        break
print(sum(a))
