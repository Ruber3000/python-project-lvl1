import random
from brain_games.game_logic import comparison
from brain_games.game_logic import is_finish_game

GAME_COUNT = 3
MIN_NUMBER = 10
MAX_NUMBER = 100


def even_find():
    print('\nAnswer \"yes\" if the number is even, otherwise answer \"no\".')
    i = 0
    while i < GAME_COUNT:
        num = random.randrange(MIN_NUMBER, MAX_NUMBER)
        answer = 'yes' if num % 2 == 0 else 'no'
        print(f'Question: {num}')
        i = comparison(answer, i, GAME_COUNT)
    is_finish_game(i, GAME_COUNT)
