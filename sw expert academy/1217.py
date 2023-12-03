"""
count == M이면 리턴
count != M : multiply
"""

T = 10


def power(N, M, count, value):
    value *= N
    count += 1
    if count == M:
        return value
    else:
        return power(N, M, count, value)


for i in range(T):
    tc = int(input())
    N, M = map(int, input().split())

    result = power(N, M, 0, 1)
    print(f"#{tc} {result}")
