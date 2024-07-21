from brain_games.core import run
from brain_games.games.prime import get_exercise, TASK
"""
Модуль для запуска игры "Проверка на числа простоту".
"""


def main():
    """
    Запускаем игру "Проверка на числа простоту".
    """
    run(get_exercise, TASK)


if __name__ == "__main__":
    main()
