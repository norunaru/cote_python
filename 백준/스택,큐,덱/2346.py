import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque(enumerate(map(int, input().split())))

ans = []

while queue:
    index, note = queue.popleft()
    ans.append(index + 1)

    if note > 0:
        queue.rotate(-(note - 1))
    elif note < 0:
        queue.rotate(-note)

print(" ".join(map(str, ans)))
