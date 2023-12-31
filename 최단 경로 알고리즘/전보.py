"""
어떤 나라에 N개의 도시가 있다.
도시가 보내고자 하는 메시지가 있는 경우 다른 도시로 전보를 보내 다른 도시로 메시지 전송할 수 있다.
하지만 X도시에서 Y도시로 전보를 보내고자 할 때, X->Y 통로가 설치되어 있어야 한다.
예를 들어 X->Y는 있지만 Y->X는 없다면 Y에서 X로 보낼 수는 없다.
통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

어느 날 C에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다.
메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것이다.

각 도시의 번호, 통로가 설치된 정보가 주어졌을 때, C에서 보낸 메시지를 받는 도시의 개수와 걸린 시간을 계산하라.

입력 조건
첫째 줄에 도시의 수 N, 통로의 개수 M, 메시지를 보내려는 도시 C가 주어진다.
(1<=N<=30000, 1<=M<=2000,000, 1<=C<=M)
둘째 줄부터 M+1번 줄에 걸쳐서 통로에 대한 정보 X,Y,Z가 주어진다.
    X->Y 비용이 Z라는 의미이다.
    (1 <= X,Y <= N, 1 <= Z <= 1000)  
3 2 1
1 2 4
1 3 2
    
출력 조건
첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
2 4
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # X번 노드에서 Y번 노드로 가는 비용이 Z라는 의미
    graph[x].append((y, z))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0

# 도달 가능한 노드 중 가장 멀리 있는 노드와의 최단거리
max_distance = 0
for d in distance:
    # 도달 가능한 노드인 경우
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)
