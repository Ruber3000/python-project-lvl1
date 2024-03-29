# functions of game's logic
import prompt


def run_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? \n')
    return name


name = run_game()
print(f'Hello, {name}!')


def comparison(answer, i, GAME_COUNT):
    answer_user = prompt.string('Your answer: ')
    answer_user = answer_user.strip().lower()
    if str(answer_user) == str(answer):
        print('Correct!\n')
        i += 1
    else:
        print(
            f'\n{answer_user} is wrong answer ;(. '
            f'Correct answer was {answer}.')
        i = GAME_COUNT + 1
    return i


def is_finish_game(i, GAME_COUNT):
    if i == GAME_COUNT:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
