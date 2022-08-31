from random import randint
from math import sqrt

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_task_and_correct_answer():
    random_number = randint(1, 100)
    correct = 'yes' if is_prime(random_number) else 'no'
    task = str(random_number)
    return task, correct
