import random
from brain_games.game_function.game_logic import welcom_user
from brain_games.game_function.game_logic import ask_name
from brain_games.game_function.game_logic import comparison
from brain_games.game_function.game_logic import is_finish_game


welcom_user()


def progress_range():
    name = ask_name()
    print('\nWhat number is missing in the progression?')
    GAME_COUNT = 3
    MIN_FIRST_NUMBER = 2
    MAX_FIRST_NUMBER = 10
    MIN_STEP = 3
    MAX_STEP = 8
    MIN_LENGHT_LIST = 6
    MAX_LENGHT_LIST = 10
    i = 0
    while i < GAME_COUNT:
        num_start = random.randrange(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
        num_step = random.randrange(MIN_STEP, MAX_STEP)
        num_lenght = random.randrange(MIN_LENGHT_LIST, MAX_LENGHT_LIST)
        num_finish = num_step * num_lenght + num_start
        list_num = list(range(num_start, num_finish, num_step))
        hide_num = random.randrange(2, len(list_num))
        answer = (list_num[hide_num - 1])
        list_num_hide1 = ' '.join([str(_) for _ in list_num[: hide_num - 1]])
        list_num_hide3 = ' '.join([str(_) for _ in list_num[hide_num:]])
        list_num_hide = list_num_hide1 + ' .. ' + list_num_hide3
        print(f'Question: {list_num_hide}')
        i = comparison(answer, i, GAME_COUNT)
    is_finish_game(i, GAME_COUNT, name)
