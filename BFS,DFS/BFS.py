from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접 노드들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 표현 - 2차원 리스트
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]


# 방문정보 표현 리스트
# 1~8노드를 가지므로 0인덱스는 사용하지 않으려고 9개로 초기화
visited = [False] * 9

# 정의된 BFS함수 호출
bfs(graph, 1, visited)
