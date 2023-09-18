"""
7 2
1 1 2 2 2 2 3
"""
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())

numbers = list(map(int, input().split()))

left_index = bisect_left(numbers, x)
right_index = bisect_right(numbers, x)

result = right_index - left_index

if result == 0:
    print(-1)
else:
    print(result)
