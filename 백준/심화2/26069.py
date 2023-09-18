import sys

n = int(input())
dance = {"ChongChong"}

for i in range(n):
    A, B = sys.stdin.readline().split()

    if A in dance:
        dance.add(B)

    if B in dance:
        dance.add(A)

print(len(dance))
