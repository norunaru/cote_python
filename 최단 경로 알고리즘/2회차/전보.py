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

# 노드 개수, 간선 개수, 시작노드 정보
node, vertex, start = map(int, input().split())

# 그래프 간 관계 표현
graph = [[] for i in range(node + 1)]

# 그래프의 출발노드에 (도착지, 비용) 정보 저장
for i in range(vertex):
    startNode, end, cost = map(int, input().split())
    graph[startNode].append((end, cost))

print(graph)

# 거리 정보는 초기에 무한대로 초기화
distance = [INF] * (node + 1)


def dijkstra(start):
    # min heap 생성
    q = []
    # 시작노드 거리를 0으로 힙에 넣음
    heapq.heappush(q, (0, start))

    # 힙이 비어있지 않으면 반복
    while q:
        # 힙에서 꺼낸 정보를 비용, 현재 처리하는 노드로 설정
        dist, now = heapq.heappop(q)
        # 힙에서 꺼낸 노드로 가는 거리가 현재 알고있는 거리보다 작다면 (이미 처리되었다면 )
        if distance[now] < dist:
            continue  # 생략
        # 현재 처리하는 노드에서 간선이 있으면
        for i in graph[now]:  # (목적지,비용) 튜플이 변수 i로 들어간다.
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))


dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
