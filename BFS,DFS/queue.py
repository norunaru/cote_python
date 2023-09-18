from collections import deque

# 큐 구현을 위해 deque라이브러리 사용
# 리스트 사용해도 되지만 시간복잡도가 더 높음. 큐 사용시 덱 라이브러리 사용하자.
queue = deque()

# 5삽입, 2삽입, 3삽입, 7삽입, 삭제, 1삽입, 4삽입, 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue)
# 역순으로 바꾸기
queue.reverse()
# 나중에 들어온 원소부터 출력
print(queue)
