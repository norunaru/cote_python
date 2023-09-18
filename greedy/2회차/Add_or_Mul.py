numbers = list(input())

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(numbers)

result = 0

for i in range(0, len(numbers)):
    if result == 0 or numbers[i] == 1 or numbers[i] == 0:
        result += numbers[i]
    else:
        result *= numbers[i]

print(result)
