#!/usr/bin/env python
from brain_games.game_engine import game_start
from brain_games.games.gcd import brain_gcd, question


def main():
    game_start(brain_gcd, question)


if __name__ == '__main__':
    main()
