import prompt
from random import randint
from math import gcd

question = 'Find the greatest common divisor of given numbers.'


def brain_gcd():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    print(f'Question: {num_1} {num_2}\n')
    answer = prompt.string('Your answer:')
    correct = str(gcd(num_1, num_2))
    return answer, correct
