import random
import math
from brain_games.games.other_files.game_logics import answer_from_user, ask_name
from brain_games.games.other_files.game_logics import check_answer, finish_game


def nod_function():
    name = ask_name()
    print('\n- Find the greatest common divisor of given numbers.')
    game_count = 3
    i = 0
    while i < game_count:
        num1, num2 = random.randrange(3, 100), random.randrange(2, 100)
        answer = math.gcd(num1, num2)
        print(f'- Question: {num1} {num2}')
        answer_user = answer_from_user()
        i = check_answer(answer_user, answer, i, game_count)
    finish_game(i, game_count, name)
