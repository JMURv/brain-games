from random import randint

GAME_QUESTION = 'What number is missing in the progression?'


def task_and_correct_answer():
    num_1 = randint(1, 10)
    num_2 = randint(40, 100)
    step = randint(2, 5)

    progression = list(range(num_1, num_2, step))
    progression = list(map(str, progression))
    point_num = randint(0, len(progression) - 1)
    correct = str(progression[point_num])
    progression[point_num] = '..'

    new_string = ' '.join(progression)
    task = f'Question: {new_string}'
    return task, correct
