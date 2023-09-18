# """
# 1 2 3 4 5 6 7

# 3
# 1 2 ? 4 5 6 7

# 6
# 1 2 ? 4 5 ? 7

# 2
# 1 ? ? 4 5 ? 7

# 7
# 1 ? ? 4 5 ? ?

# 5
# 1 ? ? 4 ? ? ?

# 1
# ? ? ? 4 ? ? ?

# 4
# ? ? ? ? ? ? ?

# startIndex + 2의 원소 제거

# 다음 startIndex는 startIndex + 2

# 만약 startIndex + 2 가 큐의 길이를 넘어선다면
# startIndex + 2 % 길이 번쨰 인덱스를 제거

# """
# from collections import deque

# n, k = map(int, input().split())
# k = k - 1
# circle = []

# for i in range(1, n + 1):
#     circle.append(i)
# startIndex = 0

# print("<", end="")
# # ==============================
# while circle:
#     length = len(circle)
#     deleteIndex = startIndex + k
#     if deleteIndex > length - 1:
#         deleteIndex = deleteIndex % length
#     print(circle.pop(deleteIndex), end="")
#     startIndex = deleteIndex
#     if circle == []:
#         break
#     print(", ", end="")
# print(">")

from collections import deque

queue = deque()
result = []

n, k = map(int, input().split())

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
        result.append(queue.popleft())
