#!/usr/bin/env python
from brain_games import game_engine
from brain_games.games import gcd


def main():
    game_engine.start(gcd)


if __name__ == '__main__':
    main()
