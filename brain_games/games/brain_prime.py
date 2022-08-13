import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    brain_prime(1)


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def brain_prime(attempt):
    num_1 = randint(1, 100)
    correct = 'yes' if is_prime(num_1) is True else 'no'
    print(f'Question: {num_1}\n')
    answer = prompt.string('Your answer: ')
    check(answer, correct, attempt)


def check(answer, correct, attempt):
    if attempt == 3:
        print(f'Correct!\nCongratulations, {name}!')

    elif answer == correct:
        print('Correct!')
        attempt += 1
        brain_prime(attempt)

    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct}."
              f"\nLet's try again, {name}!")


if __name__ == '__main__':
    main()
