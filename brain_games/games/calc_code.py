import prompt
import random


def game_calc_free():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    i = 0
    znak_list = ['+', '-', '*']
    while i < len(znak_list):
        print("\n- What is the result of the expression?")
        number1, number2 = random.randrange(1, 50), random.randrange(1, 10)
        znak = random.choice(znak_list)
        if znak == '+':
            answer = number1 + number2
        elif znak == '-':
            answer = number1 - number2
        else:
            answer = number1 * number2
        print(f'- Question: {number1} {znak} {number2}')
        answer_user = prompt.string('- Your answer: ')
        if answer_user == str(answer):
            print('- Correct!')
            i += 1
        else:
            print(
                f"\n- '{answer_user}' is wrong answer ;(. "
                "Correct answer was '{answer}'.")
            i = i + len(znak_list) + 1
            break
    if i == len(znak_list):
        print(f'\n- Congratulations, {name}!')
    else:
        print(f"- Let's try again, {name}!")
