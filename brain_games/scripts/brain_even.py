from brain_games.brain_games_main import engine
from brain_games.games.even import brain_even, question


def main():
    engine(brain_even, question)


if __name__ == '__main__':
    main()
