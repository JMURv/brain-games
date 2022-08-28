#!/usr/bin/env python
from brain_games import game_engine
from brain_games.games import even


def main():
    game_engine.start(even)


if __name__ == '__main__':
    main()
