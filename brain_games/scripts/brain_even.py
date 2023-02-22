#!/usr/bin/env python3
from brain_games.engine import manage_project
from brain_games.games import even


def main():
    manage_project(even)


if __name__ == '__main__':
    main()
