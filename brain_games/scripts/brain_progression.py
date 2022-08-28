#!/usr/bin/env python
from brain_games import game_engine
from brain_games.games import progression


def main():
    game_engine.start(progression)


if __name__ == '__main__':
    main()
