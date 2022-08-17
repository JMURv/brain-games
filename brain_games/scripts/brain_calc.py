from brain_games.brain_games_main import engine
from brain_games.games.calc import brain_calc, question


def main():
    engine(brain_calc, question)


if __name__ == '__main__':
    main()
