#!/usr/bin/env python

import prompt
# from random import randint, choice
# from brain_games.games.brain_calc import main


def main():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def check(answer, correct, attempt):
    if attempt == 3:
        print(f'Correct!\nCongratulations, {name}!')

    elif answer == correct:
        print('Correct!')
        attempt += 1
        # brain_even(attempt)
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
              f"\nLet's try again, Bill!")


if __name__ == '__main__':
    main()
