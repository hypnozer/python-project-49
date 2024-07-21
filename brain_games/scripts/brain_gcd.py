from brain_games.core import run
from brain_games.games.gcd import get_exercise, TASK
"""
Модуль для запуска игры "НОД".
"""


def main():
    """
    Запускаем игру "НОД".
    """
    run(get_exercise, TASK)


if __name__ == "__main__":
    main()
