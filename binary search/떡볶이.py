"""
떡볶이 떡의 길이가 일정하지 않다. 대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라 맞춰준다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단한다. 
높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다.

예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 
자른 뒤 떡의 높이는 15, 14, 10, 15cm가 된다. 잘린 떡의 길이는 차례대로 4,0,0,2cm이다. 
손님은 6cm 만큼의 길이를 가져간다.

손님이 왔을때 요청한 총 길이가 M일 때 
적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라

첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
둘쨰 줄에 떡의 개별 높이가 주어진다. 떡 높이 총합은 항상 M 이상이다.

적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력하라.
"""

"""

N, M = map(int, input().split())
dduck = list(map(int, input().split()))

print(dduck)

min_length = min(dduck)
max_length = max(dduck)

cutter = []

for cut_length in range(min_length, max_length):
    dduck_cut = []
    print("자르는 길이 : {}".format(cut_length))
    for i in dduck:
        if i - cut_length > 0:
            dduck_cut.append(i - cut_length)
        else:
            dduck_cut.append(0)
    print("잘린 떡 : {}, 합 : {}".format(dduck_cut, sum(dduck_cut)))
    if sum(dduck_cut) >= M:
        cutter.append(cut_length)
print(cutter)
print(max(cutter))

"""

# 절단기 높이를 크게 하면 잘린 떡의 길이가 짧아지고, 높이를 낮게 하면 잘린 떡의 길이가 길어진다.
# -> 이진 탐색 사용 가능
# 현재 이 높이로 자르면 조건을 만족하는가?를 확인한 뒤 조건의 만족 여부에 따라 탐색범위 좁혀 해결 가능.
# 절단기 높이가 0~10억이므로 큰 탐색범위에서 선형탐색 하면 안됨 -> 이진 탐색 필요

n, m = list(map(int, input().split()))

array = list(map(int, input()))

# 이진 탐색을 위한 시작점, 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 충분한 경우 더 자르기(오른쪽 부분 탐색)
    if total < x:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(왼쪽 부분 탐색)
    else:
        result = mid
        start = mid + 1

print(result)
