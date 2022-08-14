#!/usr/bin/env python
import prompt
from random import randint


def is_even(digit):
    return True if digit % 2 == 0 else False


def main():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain_even(1)


def brain_even(attempt):
    digit = randint(1, 100)
    print(f'Question: {digit}\n')
    answer = prompt.string('Your answer: ')
    correct = 'yes' if digit % 2 == 0 else 'no'
    check(answer, correct, attempt)


def check(answer, correct, attempt):
    if attempt == 3:
        print(f'Correct!\nCongratulations, {name}!'
              f"\nLet's try again, {name}!")

    elif answer == correct:
        print('Correct!')
        attempt += 1
        brain_even(attempt)
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
              f"\nLet's try again, {name}!")


if __name__ == '__main__':
    main()
