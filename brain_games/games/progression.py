from random import randint

QUESTION = 'What number is missing in the progression?'


def generate_task_and_correct_answer():
    start = randint(1, 10)
    end = randint(40, 100)
    step = randint(2, 5)

    progression = list(range(start, end, step))
    point_num = randint(0, len(progression) - 1)
    correct = str(progression[point_num])
    progression[point_num] = '..'

    new_string = ' '.join(map(str, progression))
    task = new_string
    return task, correct
