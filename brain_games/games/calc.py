import prompt
from random import randint, choice

question = 'What is the result of the expression?'


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def brain_calc():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    functions = {
        '+': plus(num_1, num_2),
        '-': minus(num_1, num_2),
        '*': mult(num_1, num_2)
    }
    operation = choice(list(functions.keys()))
    correct = str(functions[operation])
    print(f'Question: {num_1} {operation} {num_2}\n')
    answer = prompt.string('Your answer: ')
    return answer, correct
