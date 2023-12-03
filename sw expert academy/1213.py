T = 10

for i in range(T):
    tc = int(input())
    checker = input()
    inputs = input()

    result = inputs.count(checker)
    print(f"#{tc} {result}")
