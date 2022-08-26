#!/usr/bin/env python
import prompt


def game_start(game, question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    for rounds in range(3):
        question, correct = game()
        print(question)
        answer = prompt.string('Your answer: ')
        if rounds == 2 and answer == correct:
            print(f'Correct!\nCongratulations, {name}!')
        elif answer == correct:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
                  f"\nLet's try again, {name}!")
            break
