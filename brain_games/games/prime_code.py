import prompt
import random


def prime_test(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def prime_try_find():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    print(
        "\n- Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    i = 0
    while i < 3:
        num = random.randrange(1, 100)
        print(f'- Question: {num}')
        answer_user = prompt.string('- Your answer: ')
        answer_user = answer_user.strip().lower()
        answer_test = prime_test(num)
        answer = 'yes' if answer_test is True else 'no'
        if answer == answer_user:
            print('- Correct!\n')
            i += 1
        else:
            print(
                f"\n- '{answer_user}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            i = 4
    if i == 3:
        print(f'- Congratulations, {name}!')
    else:
        print(f"- Let's try again, {name}!")
