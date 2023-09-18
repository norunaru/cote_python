N = int(input())

flag = False
results = []

for i in range(N // 5 + 1):
    count = i
    sugar = N - (5 * i)

    if sugar % 3 == 0:
        count += sugar // 3
        results.append(count)
        flag = True

if flag:
    print(min(results))
else:
    print(-1)
