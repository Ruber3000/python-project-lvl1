import prompt


def welcome_user():
    name = prompt.string('- May I have your name? \n- ')
    print(f"- Hello, {name}!")
    print("- Answer \"yes\" if the number is even, otherwise answer \"no\".\n")
    answers = [15, 6, 7]
    answers_test = ['no', 'yes', 'no']
    i = 0

    while i < len(answers_test):
        print(f'- Question: {answers[i]}')
        answer_user = prompt.string('- Your answer: ')
        if answer_user == answers_test[i]:
            print('- Correct!\n')
            i += 1
        else:
            break

    if i == len(answers_test):
        print(f'- Congratulations, {name}!')
    else:
        print(
            f"\n- '{answer_user}' is wrong answer ;(. "
            f"Correct answer was '{answers_test[i]}'.")
        print(f"- Let's try again, {name}!")
