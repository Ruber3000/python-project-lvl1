import random
from brain_games.games.other_files.game_logics import answer_from_user, ask_name
from brain_games.games.other_files.game_logics import check_answer, finish_game


def game_calc_free():
    name = ask_name()

    print('\n- What is the result of the expression?')
    math_sign = ['+', '-', '*']
    game_count = 3
    i = 0
    while i < game_count:
        num1, num2 = random.randrange(1, 50), random.randrange(1, 10)
        math_sign = random.choice(math_sign)
        if math_sign == '+':
            answer = num1 + num2
        elif math_sign == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        print(f'- Question: {num1} {math_sign} {num2}')
        answer_user = answer_from_user()
        i = check_answer(answer_user, answer, i, game_count)
    finish_game(i, game_count, name)
