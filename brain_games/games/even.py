#!/usr/bin/env python
import prompt
from random import randint

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    digit = randint(1, 100)
    print(f'Question: {digit}\n')
    answer = prompt.string('Your answer: ')
    correct = 'yes' if digit % 2 == 0 else 'no'
    return answer, correct
