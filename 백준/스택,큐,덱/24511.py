"""
내가 작성한 시간 초과 코드
from collections import deque

n = int(input())

data = []
for i in range(n):
    x = deque()
    data.append(x)

dataStructure = list(map(int, input().split()))
# print("자료구조 :", dataStructure)


# 각 자료구조에 존재하는 원소 설정
numbers = list(map(int, input().split()))
for i in range(n):
    data[i].append(numbers[i])
# print("초기 단계의 자료구조 상태 :", data)

# 삽입할 수열의 길이
m = int(input())

# 삽입할 수열
inputNumbers = list(map(int, input().split()))
# print("삽입할 수열 :", inputNumbers)

results = []

# 총 m번 반복
for i in range(m):
    # 삽입할 수열중 하나씩 뺴서 첫 자료구조에 삽입
    data[0].append(inputNumbers[i])
    # 자료구조가 큐면
    if dataStructure[0] == 0:
        popData = data[0].popleft()  # 왼쪽 pop
    # 자료구조가 스택이면
    elif dataStructure[0] == 1:
        popData = data[0].pop()  # 오른쪽 pop

    # 2~n번 자료구조에 대해
    for i in range(1, n - 1):
        # 일단 앞에서 꺼낸 값을 넣어주고
        data[i].append(popData)
        # 자료구조 확인
        if dataStructure[i] == 0:
            popData = data[i].popleft()
        elif dataStructure[i] == 1:
            popData = data[i].pop()

    data[n - 1].append(popData)
    if dataStructure[n - 1] == 0:
        popData = data[n - 1].popleft()  # 왼쪽 pop
    # 자료구조가 스택이면
    elif dataStructure[n - 1] == 1:
        popData = data[n - 1].pop()  # 오른쪽 pop

    # print("{}회차 결과 : {}".format(i + 1, data))

    results.append(popData)

print(" ".join(map(str, results)))
"""

"""
스택인 부분에 값이 추가되면 어차피 그 값이 pop되므로 스택은 없는 것처럼 처리 가능하다.
큐는 여러 개의 큐가 하나의 큐처럼 작동한다.

결론적으로 스택인 부분의 숫자는 무시하고 여러개의 큐를 하나의 큐처럼 생각하여 문제 해결이 가능하다.
"""
import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
dataStructure = list(map(int, input().split()))  ## queue == 0, stack == 1
numbers = list(map(int, input().split()))  ## i번 자료구조에 들어있는 원소
M = int(input())  ## 삽입할 수열의 길이
inputNumbers = list(map(int, input().split()))  ## 삽입할 수열

## 스택은 무시하고 큐만 deque에 추가하기
queue = deque([])
for i in range(N):
    if dataStructure[i] == 0:
        queue.appendleft(numbers[i])
print(queue)

## deque가 하나의 큐 처럼 작동
for i in range(M):
    queue.append(inputNumbers[i])
    print(queue.popleft(), end=" ")
