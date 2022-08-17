import random
from brain_games.game_function.game_logics import answer_from_user, ask_name
from brain_games.game_function.game_logics import is_check_answer
from brain_games.game_function.game_logics import is_finish_game


def game_calc_free():
    name = ask_name()
    print('\nWhat is the result of the expression?')
    math_operation = ['+', '-', '*']
    num1_min, num1_max, num2_min, num2_max = 1, 100, 1, 10
    game_count = 3
    i = 0
    while i < game_count:
        num1 = random.randrange(num1_min, num1_max)
        num2 = random.randrange(num2_min, num2_max)
        math_operation = random.choice(math_operation)
        if math_operation == '+':
            answer = num1 + num2
        elif math_operation == '-':
            answer = num1 - num2
        elif math_operation == '*':
            answer = num1 * num2
        print(f'Question: {num1} {math_operation} {num2}')
        answer_user = answer_from_user()
        i = is_check_answer(answer_user, answer, i, game_count)
    is_finish_game(i, game_count, name)
