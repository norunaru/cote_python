"""
투 포인터 알고리즘은 리스트에 순차적으로 접근시 두 개의 점의 위치를 기록하면서 처리하는 알고리즘
흔히 2,3,4,5,6,7번 학생 지목시 간단히 '2번부터 7번 학생까지'라고 표현한다.
리스트에 담긴 데이터에 순차적으로 접근시 시작점, 끝점 2개의 점으로 접근할 데이터의 범위를 표현한다.

부분 연속 수열 찾기 문제에서 사용 가능
N개의 자연수로 이루어진 수열이 있다.
합이 M인 부분 연속 수열의 개수를 구하라.
1,2,3,2,5 수열이 있을때 합이 5인것을 구하려면 
(2,3) , (3,2) , (5)
수행시간 제한은 O(N)
    - 완전 탐색 이용시 O(N^2)알고리즘이 되어버린다.

투포인터 알고리즘 활용시
1. 시작점, 끝점이 첫번째 원소 인덱스를 가리키도록 한다.
2. 현재 부분 합이 M과 같다면, 카운트
3. 현재 부분 합이 M보다 작다면 end를 1증가시킨다. (현재의 부분합 증가시킴)
4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다. (현재의 부분합 감소시킴)
5. 모든 경우를 확인할 때까지 2~4과정을 반복한다.
"""

n = 5  # 데이터의 개수
m = 5  # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
