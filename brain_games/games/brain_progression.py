import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    brain_progression(1)


def brain_progression(attempt):
    num_1 = randint(1, 10)
    num_2 = randint(40, 100)
    step = randint(2, 10)

    progression = list(range(num_1, num_2, step))
    point_num = randint(0, len(progression)-1)
    correct = str(progression[point_num])

    progression[point_num] = '..'
    copy_string = str(progression)[1:-1]
    for char in copy_string:
        if char == "'" or char == ',':
            copy_string = copy_string.replace(char, '')
    print(f'Question: {copy_string}\n')
    answer = prompt.string('Your answer: ')

    check(answer, correct, attempt)


def check(answer, correct, attempt):
    if attempt == 3:
        print(f'Correct!\nCongratulations, {name}!'
              f"\nLet's try again, {name}!")

    elif answer == correct:
        print('Correct!')
        attempt += 1
        brain_progression(attempt)

    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
              f"\nLet's try again, {name}!")


if __name__ == '__main__':
    main()
