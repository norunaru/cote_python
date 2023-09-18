target = int(input())

found = False

for i in range(target):
    result = i
    i = str(i)
    strI = list(i)
    intI = list(map(int, strI))
    result += sum(intI)
    if result == target:
        found = True
        break

if found:
    print(int(i))
else:
    print(0)
