from brain_games.brain_games_main import engine
from brain_games.games.prime import brain_prime, question


def main():
    engine(brain_prime, question)


if __name__ == '__main__':
    main()
