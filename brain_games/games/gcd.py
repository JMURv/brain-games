from random import randint
from math import gcd

question = 'Find the greatest common divisor of given numbers.'


def brain_gcd():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    task = f'Question: {num_1} {num_2}'
    correct = str(gcd(num_1, num_2))
    return task, correct
