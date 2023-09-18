"""
노드의 개수가 N일 때 알고리즘 상으로 N번의 단계 수행한다.
    - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려한다.
따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N^3)이다.
"""

INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())

# 2차원 리스트를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자신에서 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    # A -> B 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# k는 거쳐 가는 노드, a는 출발 노드, b는 목적지 노드
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없으면 무한으로 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있으면 거리 출력
        else:
            print(graph[a][b], end=" ")
        print()
