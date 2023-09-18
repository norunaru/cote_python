import math


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어지면 소수가 아님
        if x % i == 0:
            return False
    return True


print(is_prime_number(4))
print(is_prime_number(7))
