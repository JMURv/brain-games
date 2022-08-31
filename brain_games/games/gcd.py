from random import randint
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'


def generate_task_and_correct_answer():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    task = f'{random_number_1} {random_number_2}'
    correct = str(gcd(random_number_1, random_number_2))
    return task, correct
