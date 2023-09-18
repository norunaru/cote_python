"""
구간 합 문제 : 연속적으로 나열된 N개의 수가 있을 떄 특정 구간의 모든 수를 합한 값을 계산하는 문제
예를 들어 5개의 데이터로 구성된 수열 {10,20,30,40,50}이 있다고 가정한다.
    두 분째 수부터 네 번째 수까지의 합은 20 + 30 + 40 = 90이다.

N개의 정수로 구성된 수열이 존재한다.
M개의 쿼리 정보가 주어진다.
    각 쿼리는 left, right로 구성
    각 쿼리에 대해 [left,right] 구간에 포함된 데이터의 합을 출력해야 한다.
수행 시간 제한은 O(M+N)이다.

*단순하게 작성시 O(M*N)이 되어버린다.
<해결 아이디어>
접두사 합(prefix sum): 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
    N개의 수 위치 각각에 대해 접두사 합을 계산하여 P에 저장한다.
    매 M개의 쿼리 정보 확인시 구간 합은 P[right] - P[left - 1]이 된다.
10 20 30 40 50 으로 prefix sum 계산

[0] [1] [2] [3] [4]  [5]
 0  10  30  60  100  150  - 시간복잡도 O(N) 으로 접두사 합을 구할 수 있다.

 left = 1, right = 3 -> P[3] - P[0] = 60
"""

# 데이터의 개수 N과 데이터 입력받기
n = 5
data = 10, 20, 30, 40, 50

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += 1
    prefix_sum.append(sum_value)

# 구간 합 계산 (세 번쨰 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
