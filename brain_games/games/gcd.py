from random import randint
from math import gcd

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def task_and_correct_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    task = f'Question: {num_1} {num_2}'
    correct = str(gcd(num_1, num_2))
    return task, correct
