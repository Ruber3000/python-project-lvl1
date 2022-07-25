import prompt
import random
import math


def nod_function():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    print("\n- Find the greatest common divisor of given numbers.")
    i = 0
    while i < 3:
        num1, num2 = random.randrange(3, 100), random.randrange(2, 100)
        answer = math.gcd(num1, num2)
        print(f'- Question: {num1} {num2}')
        answer_user = prompt.string('- Your answer: ')
        answer_user = answer_user.strip()
        if answer_user == str(answer):
            print('- Correct! \n')
            i += 1
        else:
            print(
                f"\n- '{answer_user}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            i = 4
            break
    if i == 3:
        print(f'\n- Congratulations, {name}!')
    else:
        print(f"- Let's try again, {name}!")
