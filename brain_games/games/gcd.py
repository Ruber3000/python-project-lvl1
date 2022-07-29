import prompt
import random
import math


def nod_function():
    from brain_games.games.other_files.game_logics import ask_name
    name = ask_name()
    print('\n- Find the greatest common divisor of given numbers.')
    game_count = 3
    i = 0
    while i < game_count:
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
                f'\n- {answer_user} is wrong answer ;(. '
                f'Correct answer was {answer}.')
            i = game_count + 1
            break

    from brain_games.games.other_files.game_logics import finish_game
    finish_game(i, game_count, name)
