import prompt
import random


def even_find():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    print("\n- Answer \"yes\" if the number is even, otherwise answer \"no\".")
    i = 0
    while i < 3:
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
                f"\n- '{answer_user}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            i = 4
    if i == 3:
        print(f'- Congratulations, {name}!')
    else:
        print(f"- Let's try again, {name}!")
