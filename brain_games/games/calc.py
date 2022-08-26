from random import randint, choice

question = 'What is the result of the expression?'


def brain_calc():
    num_1, num_2 = randint(1, 100), randint(1, 100)
    functions = ['+', '-', '*']
    operation = choice(functions)
    if operation == '*':
        correct = num_1 * num_2
    else:
        correct = num_1 + num_2 if operation == '+' else num_1 - num_2
    task = f'Question: {num_1} {operation} {num_2}'
    return task, str(correct)
