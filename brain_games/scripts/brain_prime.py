#!/usr/bin/env python
from brain_games import game_engine
from brain_games.games import prime


def main():
    game_engine.start(prime)


if __name__ == '__main__':
    main()
