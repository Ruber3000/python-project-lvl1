# functions for Tests


def is_prime_test(num):
    num = abs(num)
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
