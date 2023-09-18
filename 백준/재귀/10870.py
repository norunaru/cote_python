n = int(input())
n -= 1


def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n < 0:
        return 0
    else:
        return 1


print(fibonacci(n))
