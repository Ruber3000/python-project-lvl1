import prompt
import random


def game_calc_free():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    i = 0
    znak_list = ['+', '-', '*']
    while i < len(znak_list):
        print("\n- What is the result of the expression?")
        num1, num2 = random.randrange(1, 50), random.randrange(1, 10)
        znak = random.choice(znak_list)
        if znak == '+':
            answer = num1 + num2
        elif znak == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        print(f'- Question: {num1} {znak} {num2}')
        answer_user = prompt.string('- Your answer: ')
        if answer_user == str(answer):
            print('- Correct!')
            i += 1
        else:
            print(
                f"\n- '{answer_user}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            i = i + len(znak_list) + 1
            break
    if i == len(znak_list):
        print(f'\n- Congratulations, {name}!')
    else:
        print(f"- Let's try again, {name}!")
