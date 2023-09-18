n, target = map(int, input().split())
cards = list(map(int, input().split()))

cardSum = []

for x in range(n - 2):
    for y in range(x + 1, n - 1):
        for z in range(y + 1, n):
            value = cards[x] + cards[y] + cards[z]
            if value <= target:
                cardSum.append(value)
print(max(cardSum))
