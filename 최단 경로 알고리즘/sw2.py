"""
민석이네 학급에서 마니또에 참여하는 사람은 민석이를 포함해 N명이고, 1번부터 N번까지 각자 번호를 부여했다.
이 N명의 학생들은 총 M개의 마니또 관계를 맺는다.
마니또 관계를 맺는다는 의미는 한 학생이 한 학생에게 C 비용 만큼의 선물을 일방적으로 주는 것을 뜻한다. 그 반대는 해당하지 않는다.
예를 들어 X와 Y가 X → Y 마니또 관계를 맺으면, 그 반대인 X ← Y는 수행하지 않는다.

소인배인 민석이는 자신이 선물을 주는 학생과 자신에게 선물을 주는 학생, 그리고 그 사이의 모든 관계가 궁금하다.
그래서 염탐을 통해 학급의 모든 마니또 관계를 파악했고, 이를 토대로 자신이 주고 돌고 돌아 자신이 받는 마니또 사이클을 찾으려고 한다.
마니또 사이클은 시작과 끝이 같은 마니또 관계 혹은 마니또 관계들을 의미한다.
다음은 마니또 사이클을 이루는 예시이다.
  예시 1. (X → Y), (Y → Z), (Z → X)
  예시 2. (X → X)

또한 민석이는 돈도 조금 아까워 총 선물 비용이 가장 작은 마니또 사이클을 찾고 싶다.
총 선물 비용은 해당 마니또 사이클에 속하는 모든 마니또 관계의 선물 비용 합을 의미한다.

학급의 모든 마니또 관계가 주어졌을 때, 총 선물 비용이 가장 작은 마니또 사이클을 찾는 프로그램을 작성하시오.
두 학생이 주고받는 마니또 관계도 마니또 사이클에 포함됨에 주의하시오.

첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)
각 테스트 케이스의 첫 번째 줄에 학생의 수 N과 마니또 관계의 수 M이 주어진다. (2 ≤ N ≤ 400, 2 ≤ M ≤ N * (N - 1))
각 테스트 케이스의 두 번째 줄부터 M개의 줄에 걸쳐 마니또 관계의 정보 X, Y, C가 주어진다.
이는 X번 학생으로부터 Y번 학생으로 이동하는 선물 비용 C의 마니또 관계가 있다는 의미이다.

각 마니또 관계의 선물 비용은 10,000 이하의 자연수이고, 자기 자신과의 마니또 관계는 최대 한 개 등장한다. (X → X)

각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고,
총 선물 비용이 가장 작은 마니또 사이클의 비용을 출력한다.
만약, 그러한 마니또 사이클을 찾을 수 없다면 -1을 출력한다.

1      
3 4    
1 2 1  
3 2 1  
1 3 5
2 3 2

#1 3
"""


# # =================================================================
# tc = int(input())

# for i in range(tc):
#     N, M = map(int, input().split())
#     total_cost = []

#     relationship = []  # 선물 주는 관계 저장
#     graph = [[] for i in range(N + 1)]  # 각 학생이 무슨 학생과 연결되었는지 표현
#     for i in range(M):
#         x, y, c = map(int, input().split())
#         relationship.append((x, y, c))
#     print("선물 관계 :", relationship)

#     for x, y, c in relationship:
#         graph[x].append(y)
#     print("연결 관계 :", graph)

# 각 관계마다 dfs 수행
relationship = [(1, 2, 1), (3, 2, 1), (1, 3, 5), (2, 3, 2)]
graph = [[], [2, 3], [3], [2]]
total_cost = []


def dfs(start, visited, target):
    if visited[start] == True and start == target:
        total_cost.append(money)

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


for start, end, cost in relationship:
    # 매 루프마다 사용할 변수들 설정
    money = 0
    rel = relationship
    rel.remove((start, end, cost))
    visited = [False] * (N + 1)
    # 관계마다 dfs수행
    dfs(start, cost, start, visited, money, rel)
