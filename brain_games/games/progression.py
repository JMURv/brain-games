import prompt
from random import randint

question = 'What number is missing in the progression?'


def brain_progression():
    num_1 = randint(1, 10)
    num_2 = randint(40, 100)
    step = randint(2, 5)

    progression = list(range(num_1, num_2, step))
    point_num = randint(0, len(progression) - 1)
    correct = str(progression[point_num])

    progression[point_num] = '..'
    copy_string = str(progression)[1:-1]
    for char in copy_string:
        if char == "'" or char == ',':
            copy_string = copy_string.replace(char, '')
    print(f'Question: {copy_string}\n')
    answer = prompt.string('Your answer: ')

    return answer, correct
