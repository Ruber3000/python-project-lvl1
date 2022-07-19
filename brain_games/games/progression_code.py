import prompt
import random
# import math


def progress_gange():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    i = 0
    while i < 3:
        print("\n- What number is missing in the progression?")
        num_start = random.randrange(2, 10)
        num_step = random.randrange(3, 8)
        num_lenght = random.randrange(6, 10)
        num_finish = num_step * num_lenght + num_start
        list_num = list(range(num_start, num_finish, num_step))

        //////////////////
        print(
            num_start, num_finish, num_step, num_lenght, list_num)
        i = 5





        '''
        number1, number2 = random.randrange(3, 100), random.randrange(2, 100)
        answer = math.gcd(number1, number2)
        print(f'- Question: {number1} {number2}')
        answer_user = prompt.string('- Your answer: ')
        if answer_user == str(answer):
            print('- Correct!')
            i += 1
        else:
            print(
                f"\n- '{answer_user}' is wrong answer ;(. "
                "Correct answer was '{answer}'.")
            i = 4
            break
    if i == 3:
        print(f'\n- Congratulations, {name}!')
    else:
        print(f"- Let's try again, {name}!")
'''
