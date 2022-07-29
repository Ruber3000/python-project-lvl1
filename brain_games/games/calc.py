import prompt
import random
from brain_games.games.other_files.game_logics import ask_name
from brain_games.games.other_files.game_logics import finish_game


def game_calc_free():
    name = ask_name()
    print('\n- What is the result of the expression?')
    znak_list = ['+', '-', '*']
    game_count = 3
    i = 0
    while i < game_count:
        num1, num2 = random.randrange(1, 50), random.randrange(1, 10)
        math_sign = random.choice(znak_list)
        if math_sign == '+':
            answer = num1 + num2
        elif math_sign == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        print(f'- Question: {num1} {math_sign} {num2}')
        answer_user = prompt.string('- Your answer: ')
        answer_user = answer_user.strip()
        if answer_user == str(answer):
            print('- Correct!\n')
            i += 1
        else:
            print(
                f'\n- {answer_user} is wrong answer ;(. '
                f'Correct answer was {answer}.')
            i = game_count + 1
            break

    finish_game(i, game_count, name)
