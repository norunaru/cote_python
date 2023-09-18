S = list(input())

word = []
num = []

for i in S:
    if ord(i) <= 57 or ord(i) >= 49:
        num.append(i)
    else:
        word.append(i)

word = sorted(word)
num = sorted(num)

result = word + num
print(result)
