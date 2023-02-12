#!/usr/bin/env python3.
from brain_games.games import brain_calc, brain_even, brain_gcd, brain_prime, brain_progression
from brain_games.games.engine import start_game


def main():
    start_game(brain_progression)


if __name__ == '__main__':
    main()
