"""
특정 조건이 부합할 때만 사용 가능하지만 매우 빠르게 동작하는 정렬 알고리즘.
    계수 정렬은 데이터 크기 범위가 제한되어 정수 형태로 표현 가능할 때 사용 가능하다.
데이터의 개수가 N, 데이터(양수)중 최댓값이 K일 때 최악의 경우에도 수행시간 O(N+K)를 보장한다

해당 데이터가 몇 번 등장했는지 카운트하여 값 증가시킨다.
정렬할 데이터 : 7 5 9 0 3 1 6 2 9 1 4 8 0 5 2
step 0. 가장 작은 데이터부터 가장 큰 데이터까지의 범위가 모두 담길 수 있도록 리스트 생성
인덱스
0 1 2 3 4 5 6 7 8 9 
개수(count)
0 0 0 0 0 0 0 0 0 0 

step 1. 데이터를 하나씩 확인하여 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가
정렬할 데이터 : *7 5 9 0 3 1 6 2 9 1 4 8 0 5 2
개수(count)
0 0 0 0 0 0 0 1 0 0 

step 15.
2 2 2 1 1 2 1 1 1 2

결과를 확인할 때는 리스트의 첫 번째 데이터부터 하나씩 그 값을 반복하여 인덱스를 출력한다.
0 0 1 1 2 2 .... 9 9

배열이 필요하므로 공간복잡도가 높다.
"""

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=" ")  # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
"""
시간 복잡도, 공간 복잡도 모두 O(N+K)이다
계수 정렬은 때에 따라서 심각한 비효율성 초래 가능
   - 데이터가 0,999999 단 2개만 존재하는 경우
계수 정렬은 동일한 값을 가지는 데이터가 여러 번 등장할 때 효과적.
   - 성적의 경우 100점의 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적이다.
"""
