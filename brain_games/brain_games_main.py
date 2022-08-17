#!/usr/bin/env python
import prompt

name = ''


def engine(game, question):
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    answer, correct = game()
    check(game, answer, correct, 1)


def check(game, answer, correct, attempt):
    if attempt == 3:
        print(f'Correct!\nCongratulations, {name}!'
              f"\nLet's try again, {name}!")

    elif answer == correct:
        print('Correct!')
        attempt += 1
        answer, correct = game()
        check(game, answer, correct, attempt)

    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
              f"\nLet's try again, {name}!")
