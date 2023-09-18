"""
단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해 Heap자료구조 사용한다.
다익스트라 알고리즘의 동작 기본 원리는 동일하다.
    현재 가장 가까운 노드를 저장하기 위해 힙 자료구조를 추가적으로 이용한다는 점이 다르다.
    현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 이용한다.
"""

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드들을 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달 할 수 없으면 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

"""
힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)이다.
노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드 개수 V 이상 횟수로는 처리되지 않는다.
    결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는 
    최대 간선의 개수(E)만큼 연산이 수행될 수 있다.
직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사하다.
    시간 복잡도를 O(ElogE)로 판단할 수 있다.
    중복 간선을 포함하지 않는 경우 O(ElogV)로 정리 가능하다.
"""
