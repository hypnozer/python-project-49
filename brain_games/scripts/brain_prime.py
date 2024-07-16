from brain_games.core import get_scenario
from brain_games.games.prime import get_exercise, task


def main():
    get_scenario(get_exercise, task)


if __name__ == "__main__":
    main()
