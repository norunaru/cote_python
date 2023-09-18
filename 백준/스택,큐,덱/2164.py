from collections import deque

n = int(input())

cards = deque()

for i in range(1, n + 1):
    cards.append(i)

cards.reverse()

while len(cards) != 1:
    cards.pop()
    cards.rotate(1)

print(cards[0])
