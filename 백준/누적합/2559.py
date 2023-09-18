"""
인덱싱 사용하면 시간 초과

3 -2 -4 -9   0   3   7  13 8   -3
3  1 -3 -12 -12 -9  -2  11 19  16
"""

n, k = map(int, input().split())

temprature = list(map(int, input().split()))


a = 0
tempsum = [0]

for i in temprature:
    a += i
    tempsum.append(a)

results = []

idx = 0
while idx != len(temprature) - k + 1:
    results.append(tempsum[idx + k] - tempsum[idx])
    idx += 1

print(max(results))
