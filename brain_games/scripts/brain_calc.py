from brain_games.core import get_scenario
from brain_games.games.calc import get_exercise, TASK
"""
Модуль для запуска игры "Калькулятор".
"""


def main():
    """
    Запускаем игру "Калькулятор".
    """
    get_scenario(get_exercise, TASK)


if __name__ == "__main__":
    main()
