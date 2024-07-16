from brain_games.core import get_scenario
from brain_games.games.gcd import get_exercise, TASK
"""
Модуль для запуска игры "НОД".
"""


def main():
    """
    Запускаем игру "НОД".
    """
    get_scenario(get_exercise, TASK)


if __name__ == "__main__":
    main()
