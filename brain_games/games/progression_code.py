import prompt
import random


def progress_range():
    from brain_games.games.other_files.game_logics import ask_name
    name = ask_name()
    print("\n- What number is missing in the progression?")
    game_rounds = 3
    i = 0
    while i < game_rounds:
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
        answer_user = prompt.string('- Your answer: ')
        answer_user = answer_user.strip()
        if answer_user == str(answer):
            print('- Correct!\n')
            i += 1
        else:
            print(
                f"\n- '{answer_user}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            i = game_rounds + 1
            break

    from brain_games.games.other_files.game_logics import finish_game
    finish_game(i, game_rounds, name)
