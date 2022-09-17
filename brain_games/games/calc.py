import random
from brain_games.game_logic import comparison
from brain_games.game_logic import is_finish_game

GAME_COUNT = 3
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 100
MIN_SECOND_NUMBER = 1
MAX_SECOND_NUMBER = 10

print('\nWhat is the result of the expression?')
math_operation = ['+', '-', '*']
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
    i = comparison(answer, i, GAME_COUNT)


def game_calc_free():
    is_finish_game(i, GAME_COUNT)
