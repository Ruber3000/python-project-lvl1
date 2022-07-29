import prompt
import random


def even_find():
    from brain_games.games.other_files.game_logics import ask_name
    name = ask_name()
    print('\n- Answer \"yes\" if the number is even, otherwise answer \"no\".')
    game_count = 3
    i = 0
    while i < game_count:
        num = random.randrange(10, 100)
        answer = 'yes' if num % 2 == 0 else 'no'
        print(f'- Question: {num}')
        answer_user = prompt.string('- Your answer: ')
        answer_user = answer_user.strip().lower()
        if answer == str(answer_user):
            print('- Correct!\n')
            i += 1
        else:
            print(
                f'\n- {answer_user} is wrong answer ;(. '
                f'Correct answer was {answer}.')
            i = game_count + 1

    from brain_games.games.other_files.game_logics import finish_game
    finish_game(i, game_count, name)
