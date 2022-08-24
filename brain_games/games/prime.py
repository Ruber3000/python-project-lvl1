import random
from brain_games.game_function.game_logic import welcom_user
from brain_games.game_function.game_logic import ask_name
from brain_games.game_function.game_logic import comparison
from brain_games.game_function.game_logic import is_finish_game
from brain_games.game_function.tests import is_prime_test


def prime_try_find():
    welcom_user()
    name = ask_name()
    print(
        '\nAnswer \"yes\" if given number is prime. Otherwise answer \"no\".')
    GAME_COUNT = 3
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    i = 0
    while i < GAME_COUNT:
        num = random.randrange(MIN_NUMBER, MAX_NUMBER)
        answer_test = is_prime_test(num)
        answer = 'yes' if answer_test is True else 'no'
        print(f'Question: {num}')
        i = comparison(answer, i, GAME_COUNT)
    is_finish_game(i, GAME_COUNT, name)
