"""
N x M 크기의 얼음 틀이 있다. 구멍이 뚫린 부분이 0, 칸막이가 존재하는 부분은 1로 표시된다. 
구멍이 뚫린 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결된 것으로 간주한다. 
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
다음과 같은 4*5 얼음틀 예시에서는 총 3개 생성된다.
00110
00011
11111
00000

첫째 줄에 세로 길이 N, 가로 길이 M이 주어진다.
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.

한번에 만들 수 있는 개수를 출력하라.
"""
"""
n, m = map(int, input().split())
count = 0
# 얼음틀
block = []
for i in range(n):
    block.append(list(input()))
print(block)

#BFS
"""

# DFS
# 특정 지점의 상하좌유 살핀 뒤 주변 지점에 값이 0이고 아직 방문하지 않은 지점이 있다면 해당 지점 방문
# 방문한 지점에서 상하좌우 다시 살피면서 방문과정 반복, 연결된 모든 지점 방문하게됨.
# 모든 노드에 대해 위의 과정을 반복하며 방문하지 않은 지점의 수 카운트


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리, True반환하게함.
        graph[x][y] = 1
        # 상하좌우 재귀적 호출
        # 여기서 하는 dfs는 리턴값이 없으므로 단순히 연결된 모든 노드에 대해 방문처리하는것(result값 증가 x)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# N,M을 공백 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS수행, 방문한 노드라면 카운트 증가
        if dfs(i, j) == True:
            result += 1

print(result)
