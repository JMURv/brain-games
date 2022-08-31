from random import randint

RULES = 'What number is missing in the progression?'


def generate_task_and_correct_answer():
    start = randint(1, 10)
    end = randint(40, 100)
    step = randint(2, 5)

    progression = list(range(start, end, step))
    point_num = randint(0, len(progression) - 1)
    correct = str(progression[point_num])
    progression[point_num] = '..'

    task = ' '.join(map(str, progression))
    return task, correct
