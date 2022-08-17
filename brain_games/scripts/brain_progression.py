from brain_games.brain_games_main import engine
from brain_games.games.progression import brain_progression, question


def main():
    engine(brain_progression, question)


if __name__ == '__main__':
    main()
