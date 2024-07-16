from brain_games.core import get_scenario
from brain_games.games.even import get_exercise, TASK
"""
Модуль для запуска игры "Проверка на четность".
"""


def main():
    """
    Запускаем игру "Проверка на четность".
    """
    get_scenario(get_exercise, TASK)


if __name__ == "__main__":
    main()
