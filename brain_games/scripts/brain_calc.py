#!usr/bin/env python3

from brain_games.engine import game_logic
from brain_games.games.calc import get_exercise, task


def main():
    game_logic(get_exercise, task)


if __name__ == "__main__":
    main()
