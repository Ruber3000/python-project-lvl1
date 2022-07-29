import random
from brain_games.games.other_files.game_logics import answer_from_user, ask_name
from brain_games.games.other_files.game_logics import check_answer, finish_game


def progress_range():
    name = ask_name()
    print('\n- What number is missing in the progression?')
    game_count = 3
    i = 0
    while i < game_count:
        num_start = random.randrange(2, 10)
        num_step = random.randrange(3, 8)
        num_lenght = random.randrange(6, 10)
        num_finish = num_step * num_lenght + num_start
        list_num = list(range(num_start, num_finish, num_step))
        hide_num = random.randrange(2, len(list_num))
        answer = (list_num[hide_num - 1])
        list_num_hide1 = " ".join([str(_) for _ in list_num[: hide_num - 1]])
        list_num_hide3 = " ".join([str(_) for _ in list_num[hide_num:]])
        list_num_hide = list_num_hide1 + " .. " + list_num_hide3
        print(f'Question: {list_num_hide}')
        answer_user = answer_from_user()
        i = check_answer(answer_user, answer, i, game_count)
    finish_game(i, game_count, name)
