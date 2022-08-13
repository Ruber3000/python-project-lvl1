import random
from brain_games.game_function.game_logics import answer_from_user, ask_name
from brain_games.game_function.game_logics import check_answer, finish_game


def even_find():
    name = ask_name()
    print('\nAnswer \"yes\" if the number is even, otherwise answer \"no\".')
    game_count = 3
    num_min, num_max = 10, 100
    i = 0
    while i < game_count:
        num = random.randrange(num_min, num_max)
        answer = 'yes' if num % 2 == 0 else 'no'
        print(f'Question: {num}')
        answer_user = answer_from_user()
        i = check_answer(answer_user, answer, i, game_count)
    finish_game(i, game_count, name)
