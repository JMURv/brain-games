import prompt

ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_QUESTION)
    for _round in range(ROUNDS):
        question, correct = game.task_and_correct_answer()
        print(question)
        answer = prompt.string('Your answer: ')

        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'.\n"
                f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
