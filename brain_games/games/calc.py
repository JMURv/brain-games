from random import randint, choice

QUESTION = 'What is the result of the expression?'


def generate_task_and_correct_answer():
    num_1, num_2 = randint(1, 100), randint(1, 100)
    operators = ['+', '-', '*']
    operation = choice(operators)
    if operation == '*':
        correct = num_1 * num_2
    elif operation == '+':
        correct = num_1 + num_2
    elif operation == '-':
        correct = num_1 - num_2
    task = f'{num_1} {operation} {num_2}'
    return task, str(correct)
