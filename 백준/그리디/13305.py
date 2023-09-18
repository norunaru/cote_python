"""
4 
2 3 1
5 2 4 1

A  ->  B  ->  C  ->  D
5 (2)  2 (3)  4 (1)  1
# """
# n = int(input())
# roads = list(map(int, input().split()))
# gasPrice = list(map(int, input().split()))

# result = roads[0] * gasPrice[0]
# minPrice = gasPrice[0]
# distance = 0

# for i in range(1, n - 1):
#     if gasPrice[i] < minPrice:  # 현재 도착한 도시의 기름값이 이전 도시들보다 싸다면
#         result += minPrice * distance  # 현재 도착한 도시 직전의 도시의 기름값 * 주행거리를 결과에 더한다.
#         distance = roads[i]
#         minPrice = gasPrice[i]
#     else:
#         distance += roads[i]
#     if i == n - 2:
#         result += minPrice * distance
# print(result)


n = int(input())
roads = list(map(int, input().split()))
gasPrice = list(map(int, input().split()))

result = 0
minPrice = gasPrice[0]

for i in range(n - 1):
    if gasPrice[i] < minPrice:
        minPrice = gasPrice[i]
    result += minPrice * roads[i]
print(result)
