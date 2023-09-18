N = int(input())

travlers = map(int, input().split())

travlers = sorted(travlers, reverse=True)
print(travlers)

count = 0

for i in travlers:
    if len(travlers) < i:
        break
    travlers = travlers[i:]
    print(travlers)
    count += 1

print(count)
