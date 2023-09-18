"""
미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
방문 판매원 A는 1번 회사에 위치해 있으며 X번 회사에 방문해 물건을 판매하고자 한다.

특정 회사에 도착하기 위한 방법은 회사끼리 연결된 도로를 이용하는 것이다. 
또한 연결된 2개의 회사는 양방향으로 이동 가능하다.
특정 회사와 다른 회사가 도로로 연결되어 있다면, 정확히 1만큼의 시간으로 이동할 수 있다.

방문 판매원은 K회사에서 소개팅한 뒤 X회사로 가려고 한다.
1 -> K -> X로 가는 최소 시간을 계산하는 프로그램을 작성하라.

입력 : 
첫째 줄에 전체 회사의 개수 N, 경로의 개수 M이 공백으로 구분되어 주어진다.
1 <= N, M <= 100

둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
M+2 번째 줄에는 X와 K가 공백으로 구분되어 주어진다. 1 <= K <= 100
5 7
1 2
1 3
1 4 
2 4 
3 4
3 5
4 5
4 5
(마지막 4,5는 X,K이다.)

출력 : 
첫째 줄에 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
만약 X번 회사에 도달할 수 없으면 -1을 출력한다.
"""
INF = 9
N, M = map(int, input().split())

distance = [[INF for i in range(N + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    distance[i][i] = 0

for i in range(M):
    start, end = map(int, input().split())
    distance[start][end] = 1
    distance[end][start] = 1

for i in range(N + 1):
    print(distance[i])

x, k = map(int, input().split())

for middle_city in range(1, N + 1):
    for start in range(1, N + 1):
        for end in range(1, N + 1):
            distance[start][end] = min(
                distance[start][end],
                distance[start][middle_city] + distance[middle_city][end],
            )


for i in range(N + 1):
    print(distance[i])

print(distance[1][k] + distance[k][x])
