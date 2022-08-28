#!/usr/bin/env python
from brain_games import game_engine
from brain_games.games import calc


def main():
    game_engine.start(calc)


if __name__ == '__main__':
    main()
