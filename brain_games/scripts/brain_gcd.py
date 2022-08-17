from brain_games.brain_games_main import engine
from brain_games.games.gcd import brain_gcd, question


def main():
    engine(brain_gcd, question)


if __name__ == '__main__':
    main()
