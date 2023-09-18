"""
단계마다 방문하지 않은 노드 중에 최단 거리가 가장 짧은 노드를 선택하기 위해 
매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)한다.
"""

import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한대값을 10억으로 설정

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모드 무한으로 초기화
distance = [INF] * (n + 1)


# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append(b, c)


# 방문하지 않은 노드 중에 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    # 출발 노드부터 당장 갱신이 가능한 노드들 거리 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 시작
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[i]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 알고리즘 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INFINITIY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])

"""
O(V)번에 걸쳐 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다.
따라서 전체 시간 복잡도는 O(V^2)이다.
일반적으로 코테의 최단 경로 문제에서 전체 노드 개수가 5000개 이하라면 이 코드로 문제 해결이 가능하다.
    - 만약 노드 개수가 10000개 이상이라면 어떻게 해결해야 할까? (약 1억번 이상의 연산)
    - 더욱 효율적인 알고리즘 설계 필요.

우선순위 큐 :
여러 개의 데이터 중 가장 우선순위가 높은 데이터부터 꺼내서 확인해야 하는 경우 사용한다.
표준 라이브러리 형태로 지원한다.
우선순위 큐 구현을 위해 Heap 자료구조를 이용한다 
        삽입 시간       삭제 시간
리스트      1              N 
힙        logN          logN   
"""
