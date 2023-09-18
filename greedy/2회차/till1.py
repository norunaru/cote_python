# N, M = map(int, input().split())
# count = 0

# while N != 1:
#     if N % M == 0:
#         N //= M
#         count += 1
#     else:
#         N -= 1
#         count += 1

# print(count)

n, k = map(int, input().split())

result = 0

while True:
    # k로 나누어 떨어지는 n과 가장 가까운 값을 찾는다.
    # ex) 23,3 이면 21이 되고, 23-21 = 2 만큼만 1 빼는 연산 수행하면 된다.
    target = (n // k) * k
    result += n - target
    n = target  # k로 나누어지는 가장 가까운 값으로 대체

    if n < k:
        break
    result += 1
    n //= k
