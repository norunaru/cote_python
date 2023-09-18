import sys, math

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
remainder = [0] * m

temp = 0
count = 0

for i in numbers:
    temp += i
    remainder[temp % m] += 1

for i in remainder:
    if i >= 2:
        count += math.comb(i, 2)

count += remainder[0]

print(count)
