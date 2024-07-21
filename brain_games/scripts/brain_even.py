from brain_games.core import run
from brain_games.games.even import get_exercise, TASK
"""
Модуль для запуска игры "Проверка на четность".
"""


def main():
    """
    Запускаем игру "Проверка на четность".
    """
    run(get_exercise, TASK)


if __name__ == "__main__":
    main()
