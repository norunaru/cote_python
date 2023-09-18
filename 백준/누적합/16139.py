import sys

input = sys.stdin.readline

alphabets = {}

for i in range(97, 97 + 26):
    alphabets[chr(i)] = 0


results = [alphabets.copy()]

string = list(input().rstrip())

for c in string:
    alphabets[c] += 1
    results.append(alphabets.copy())


q = int(input())

for i in range(q):
    abc, start, end = input().split()
    start = int(start)
    end = int(end) + 1
    print(results[end][abc] - results[start][abc])
