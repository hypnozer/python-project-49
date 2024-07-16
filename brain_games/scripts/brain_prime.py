from brain_games.core import start_game
from brain_games.games.prime import get_exercise, task


def main():
    start_game(get_exercise, task)


if __name__ == "__main__":
    main()
