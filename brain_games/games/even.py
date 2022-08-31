from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_task_and_correct_answer():
    digit = randint(1, 100)
    task = str(digit)
    correct = 'yes' if digit % 2 == 0 else 'no'
    return task, correct
