import prompt
from random import randint, choice

name = ''


def main():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    brain_calc(1)


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def brain_calc(attempt):
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
    check(answer, correct, attempt)


def check(answer, correct, attempt):
    if attempt == 3:
        print(f'Correct!\nCongratulations, {name}!'
              f"\nLet's try again, {name}!")

    elif answer == correct:
        print('Correct!')
        attempt += 1
        brain_calc(attempt)

    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
              f"\nLet's try again, {name}!")


if __name__ == '__main__':
    main()
