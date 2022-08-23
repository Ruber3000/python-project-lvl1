import random
import math
from brain_games.game_function.game_logics import answer_from_user, ask_name
from brain_games.game_function.game_logics import is_check_answer
from brain_games.game_function.game_logics import is_finish_game


def nod_function():
    name = ask_name()
    print('\nFind the greatest common divisor of given numbers.')
    GAME_COUNT = 3
    MIN_FIRST_NUMBER = 3
    MAX_FIRST_NUMBER = 100
    MIN_SECOND_NUMBER = 2
    MAX_SECOND_NUMBER = 100
    i = 0
    while i < GAME_COUNT:
        num1 = random.randrange(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
        num2 = random.randrange(MIN_SECOND_NUMBER, MAX_SECOND_NUMBER)
        answer = math.gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        answer_user = answer_from_user()
        i = is_check_answer(answer_user, answer, i, GAME_COUNT)
    is_finish_game(i, GAME_COUNT, name)
