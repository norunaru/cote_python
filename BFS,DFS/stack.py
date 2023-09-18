stack = []

# append, pop의 시간복잡도는 O(1)
# 5삽입, 2삽입, 3삽입, 7삽입, 삭제, 1삽입, 4삽입, 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 최상단 원소부터 출력
print(stack[::-1])
# 최하단 원소부터 출력
print(stack)
