import random
from brain_games.game_function.game_logics import answer_from_user, ask_name
from brain_games.game_function.game_logics import is_check_answer
from brain_games.game_function.game_logics import is_finish_game


def game_calc_free():
    name = ask_name()
    print('\nWhat is the result of the expression?')
    GAME_COUNT = 3
    math_operation = ['+', '-', '*']
    MIN_FIRST_NUMBER = 1
    MAX_FIRST_NUMBER = 100
    MIN_SECOND_NUMBER = 1
    MAX_SECOND_NUMBER = 10
    i = 0
    while i < GAME_COUNT:
        num1 = random.randrange(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
        num2 = random.randrange(MIN_SECOND_NUMBER, MAX_SECOND_NUMBER)
        math_operation_choice = random.choice(math_operation)
        if math_operation_choice == '+':
            answer = num1 + num2
        elif math_operation_choice == '-':
            answer = num1 - num2
        elif math_operation_choice == '*':
            answer = num1 * num2
        print(f'Question: {num1} {math_operation_choice} {num2}')
        answer_user = answer_from_user()
        i = is_check_answer(answer_user, answer, i, GAME_COUNT)
    is_finish_game(i, GAME_COUNT, name)
