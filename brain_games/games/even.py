from random import randint

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    digit = randint(1, 100)
    task = f'Question: {digit}'
    correct = 'yes' if digit % 2 == 0 else 'no'
    return task, correct
