# additional function


def prime_test(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
