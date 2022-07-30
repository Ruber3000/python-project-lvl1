import random
from brain_games.games.other_files.game_logics import answer_from_user, ask_name
from brain_games.games.other_files.game_logics import check_answer, finish_game
from brain_games.games.other_files.my_function import prime_test


def prime_try_find():
    name = ask_name()
    print(
        '\n- Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    game_count = 3
    i = 0
    while i < game_count:
        num = random.randrange(1, 100)
        answer_test = prime_test(num)
        answer = 'yes' if answer_test is True else 'no'
        print(f'- Question: {num}')
        answer_user = answer_from_user()
        i = check_answer(answer_user, answer, i, game_count)

    finish_game(i, game_count, name)
