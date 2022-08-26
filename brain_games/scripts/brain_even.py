#!/usr/bin/env python
from brain_games.game_engine import game_start
from brain_games.games.even import brain_even, question


def main():
    game_start(brain_even, question)


if __name__ == '__main__':
    main()
