import sys

input = sys.stdin.read


def cantore(str, n):
    if n == 0:
        print(str)
        return
    cantore(str + " " * len(str) + str, n - 1)


for i in input().split():
    cantore("-", int(i))
