from random import randint

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def brain_prime():
    num_1 = randint(1, 100)
    correct = 'yes' if is_prime(num_1) is True else 'no'
    task = f'Question: {num_1}'
    return task, correct
