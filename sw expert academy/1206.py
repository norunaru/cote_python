T = 10
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))

    allCount = 0

    for j in range(2, N - 2):
        leftMax = max(buildings[j - 2], buildings[j - 1])
        rightMax = max(buildings[j + 2], buildings[j + 1])
        if buildings[j] < leftMax or buildings[j] < rightMax:
            continue
        else:
            currentMax = leftMax if leftMax > rightMax else rightMax
            allCount += buildings[j] - currentMax
    print(f"#{test_case} {allCount}")
