# common function

def ask_name():
    import prompt
    name = prompt.string('- May I have your name? \n- ')
    print(f'- Hello, {name}!')
    return(name)


def finish_game(i, game_count, name):
    if i == game_count:
        print(f'- Congratulations, {name}!')
    else:
        print(f"- Let's try again, {name}!")


def prime_test(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
