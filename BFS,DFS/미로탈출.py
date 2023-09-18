"""
N x M 크기의 직사강형 형태의 미로에 갇혔다. 미로에는 여러 괴물이 있어 피해 탈출해야 한다.
시작 위치는 1,1이며 미로의 출구는 N,M위치에 존재하여 한번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 곳은 0, 없는 곳은 1로 표시되었다.
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 칸을 셀 때는 시작 칸, 마지막 칸 모두 포함해 계산한다. 

첫째 줄에 N, M이 주어진다.
다음 N개 줄에 0,1로 미로 정보가 주어진다. 각각의 수는 공백 없이 붙어서 입력으로 제시된다.
시작칸, 마지막 칸은 항상 1이다
101010
111111
000001
111111
111111

답 : 10
"""

"""
BFS 사용 - BFS는 시작 지점부터 가까운 노드부터 차례대로 모든 노드 탐색
1,1 부터 BFS수행하여 모든 노드의 최단거리값 기록하면 해결 가능하다.
"""
from collections import deque


def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행 결과 출력
print(bfs(0, 0))
