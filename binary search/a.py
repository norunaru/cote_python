from bisect import bisect_left, bisect_right


# bisect_left는 그 원소의 위치 반환, bisect_right는 그 원소의 다음 위치 반환
def count_by_range(a, left_val, right_val):
    right_index = bisect_right(a, right_val)
    left_index = bisect_left(a, left_val)
    print(left_index)
    print(right_index)
    return right_index - left_index


a = [1, 2, 2, 3, 3, 4, 4, 5, 6]

print(count_by_range(a, 3, 3))
