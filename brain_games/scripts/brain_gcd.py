from brain_games.core import get_scenario
from brain_games.games.gcd import get_exercise, task
"""
Модуль для запуска игры "НОД".
"""


def main():
    """
    Запускаем игру "НОД".
    """
    get_scenario(get_exercise, task)


if __name__ == "__main__":
    main()
