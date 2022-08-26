#!/usr/bin/env python
from brain_games.game_engine import game_start
from brain_games.games.prime import brain_prime, question


def main():
    game_start(brain_prime, question)


if __name__ == '__main__':
    main()
