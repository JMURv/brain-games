import prompt
from random import randint
from math import gcd


def main():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    brain_gcd(1)


def brain_gcd(attempt):
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    print(f'Question: {num_1} {num_2}\n')
    answer = prompt.string('Your answer:')
    correct = str(gcd(num_1, num_2))
    check(answer, correct, attempt)


def check(answer, correct, attempt):
    if attempt == 3:
        print(f'Correct!\nCongratulations, {name}!'
              f"\nLet's try again, {name}!")

    elif answer == correct:
        print('Correct!')
        attempt += 1
        brain_gcd(attempt)

    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
              f"\nLet's try again, {name}!")


if __name__ == '__main__':
    main()
