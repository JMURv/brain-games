#!/usr/bin/env python
from brain_games.game_engine import game_start
from brain_games.games.calc import brain_calc, question


def main():
    game_start(brain_calc, question)


if __name__ == '__main__':
    main()
