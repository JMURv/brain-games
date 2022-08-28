from random import randint

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def task_and_correct_answer():
    digit = randint(1, 100)
    task = f'Question: {digit}'
    correct = 'yes' if digit % 2 == 0 else 'no'
    return task, correct
