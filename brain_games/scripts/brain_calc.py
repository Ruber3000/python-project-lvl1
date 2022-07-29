#!/usr/bin/env python

print('Welcome to the Brain Games!')


def main():
    from ..games.calc import game_calc_free
    game_calc_free()


if __name__ == '__main__':
    main()
