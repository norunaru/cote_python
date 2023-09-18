n, m = map(int, input().split())

# 화폐 단위를 가진 리스트
coins = []

for i in range(n):
    coins.append(int(input()))

d = [10001] * (m + 1)


d[0] = 0

for coin in coins:
    for j in range(coin, m + 1):
        if d[j - coin] != 10001:
            d[j] = min(d[j], d[j - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
