import random
from brain_games.game_logic import welcom_user
from brain_games.game_logic import ask_name
from brain_games.game_logic import comparison
from brain_games.game_logic import is_finish_game


def even_find():
    welcom_user()
    name = ask_name()
    print('\nAnswer \"yes\" if the number is even, otherwise answer \"no\".')
    GAME_COUNT = 3
    MIN_NUMBER = 10
    MAX_NUMBER = 100
    i = 0
    while i < GAME_COUNT:
        num = random.randrange(MIN_NUMBER, MAX_NUMBER)
        answer = 'yes' if num % 2 == 0 else 'no'
        print(f'Question: {num}')
        i = comparison(answer, i, GAME_COUNT)
    is_finish_game(i, GAME_COUNT, name)
