#!/usr/bin/env python
from brain_games.game_engine import game_start
from brain_games.games.progression import brain_progression, question


def main():
    game_start(brain_progression, question)


if __name__ == '__main__':
    main()
