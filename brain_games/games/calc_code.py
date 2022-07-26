import prompt
import random


def game_calc_free():
    from brain_games.games.other_files.game_logics import ask_name
    name = ask_name()
    print("\n- What is the result of the expression?")
    znak_list = ['+', '-', '*']
    game_rounds = 3
    i = 0
    while i < game_rounds:
        num1, num2 = random.randrange(1, 50), random.randrange(1, 10)
        znak = random.choice(znak_list)
        if znak == '+':
            answer = num1 + num2
        elif znak == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        print(f'- Question: {num1} {znak} {num2}')
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
