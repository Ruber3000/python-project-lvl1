import random
from brain_games.game_logic import comparison
from brain_games.game_logic import is_finish_game
from brain_games.tests.tests import is_prime_test

GAME_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 100

print('\nAnswer \"yes\" if given number is prime. Otherwise answer \"no\".')
i = 0
while i < GAME_COUNT:
    num = random.randrange(MIN_NUMBER, MAX_NUMBER)
    answer_test = is_prime_test(num)
    answer = 'yes' if answer_test is True else 'no'
    print(f'Question: {num}')
    i = comparison(answer, i, GAME_COUNT)


def prime_try_find():
    is_finish_game(i, GAME_COUNT)
