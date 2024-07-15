#!usr/bin/env python3

from brain_games.core import scenario
from brain_games.games.even import get_exercise, task


def main():
    scenario(get_exercise, task)


if __name__ == "__main__":
    main()
