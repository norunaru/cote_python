"""
스택1이 비어있지 않으면 스택1의 최상단이 count인지 확인, 맞으면 pop, 아니면 스택2로 넘김
(초기에 스택1은 몇개가 들어있고, 반복문이 끝나면 스택1이 비게됨.)
스택2가 비어있지 않고 스택2의 최상단이 count면 제거

모든 반복문이 끝난 뒤 스택2가 비어있지 않다면 순서대로 나가지 못한것이므로 Sad출력
"""

from collections import deque

n = int(input())
stack1 = deque(map(int, input().split()))
stack2 = deque()
count = 1

# 스택1이 비어있지 않으면 반복
while stack1:
    # 스택 1이 비어있지 않고 스택1의 최상단이 카운트면
    if stack1 and stack1[0] == count:
        # 스택1의 최상단 제거
        stack1.popleft()
        count += 1
    # 스택1이 비어있거나 스택1의 최상단이 카운트가 아니면
    else:
        # 스택 2에 넣어준다
        stack2.append(stack1.popleft())
    # 스택2가 비어있지 않고 스택2의 최상단이 카운트면
    while stack2 and stack2[-1] == count:
        # 스택2에서 하나 제거
        stack2.pop()
        count += 1


if stack2 != []:
    print("Sad")
else:
    print("Nice")
