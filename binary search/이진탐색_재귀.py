def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        binary_search(array, target, start, mid - 1)
    else:
        binary_search(array, target, mid + 1, end)


# n(원소의 개수)과 target(찾는 값)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print("{}번째 위치에서 원소 발견".format(result + 1))
