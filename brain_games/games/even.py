import random
from brain_games.game_function.game_logics import answer_from_user, ask_name
from brain_games.game_function.game_logics import is_check_answer
from brain_games.game_function.game_logics import is_finish_game


def even_find():
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
        answer_user = answer_from_user()
        i = is_check_answer(answer_user, answer, i, GAME_COUNT)
    is_finish_game(i, GAME_COUNT, name)
