# 파이썬은 최소 힙은 제공하지만 최대 힙은 제공하지 않음

import heapq


# 내림차순 힙 정렬(heap sort)
def heapSort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # 넣을 때 부호를 바꿔서 넣고
    # 힙에 삽입된 모든 원소들을 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))  # 꺼낼 때 부호 바꿔 꺼낸다
    return result


result = heapSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
