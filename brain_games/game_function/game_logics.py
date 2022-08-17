# common function
import prompt


def word_welcome():
    print('Welcome to the Brain Games!')


def ask_name():
    name = prompt.string('May I have your name? \n')
    print(f'Hello, {name}!')
    return name


def answer_from_user():
    answer_user = prompt.string('Your answer: ')
    answer_user = answer_user.strip().lower()
    return answer_user


def is_check_answer(answer_user, answer, i, game_count):
    if str(answer_user) == str(answer):
        print('Correct!\n')
        i += 1
    else:
        print(
            f'\n{answer_user} is wrong answer ;(. '
            f'Correct answer was {answer}.')
        i = game_count + 1
    return i


def is_finish_game(i, game_count, name):
    if i == game_count:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
