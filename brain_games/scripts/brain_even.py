#!usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.even import get_exercise, task


def main():
    engine(get_exercise, task)


if __name__ == "__main__":
    main()
