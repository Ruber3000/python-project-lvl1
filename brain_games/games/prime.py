import prompt
import random


def prime_try_find():
    from brain_games.games.other_files.game_logics import ask_name
    name = ask_name()
    print(
        '\n- Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    game_count = 3
    i = 0
    while i < game_count:
        num = random.randrange(1, 100)
        print(f'- Question: {num}')
        answer_user = prompt.string('- Your answer: ')
        answer_user = answer_user.strip().lower()
        from brain_games.games.other_files.game_logics import prime_test
        answer_test = prime_test(num)
        answer = 'yes' if answer_test is True else 'no'
        if answer == answer_user:
            print('- Correct!\n')
            i += 1
        else:
            print(
                f'\n- {answer_user} is wrong answer ;(. '
                f'Correct answer was {answer}.')
            i = game_count + 1

    from brain_games.games.other_files.game_logics import finish_game
    finish_game(i, game_count, name)
