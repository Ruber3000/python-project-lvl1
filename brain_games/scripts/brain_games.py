#!/usr/bin/env python

print('Welcome to the Brain Games!')


def main():
    from ..games.cli import welcome_user
    welcome_user()


if __name__ == '__main__':
    main()
