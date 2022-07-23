import prompt
import random


def progress_range():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    i = 0
    while i < 3:
        print("\n- What number is missing in the progression?")
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
        if answer_user == str(answer):
            print('- Correct!')
            i += 1
        else:
            print(
                f"\n- '{answer_user}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            i = 4
            break
        if i == 3:
            print(f'\n- Congratulations, {name}!')
        else:
            print(f"- Let's try again, {name}!")
