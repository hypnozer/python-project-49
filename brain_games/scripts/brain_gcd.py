from brain_games.core import get_brain_game
from brain_games.games.gcd import get_exercise, task


def main():
    get_brain_game(get_exercise, task)


if __name__ == "__main__":
    main()
