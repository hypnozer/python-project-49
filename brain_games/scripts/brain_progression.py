from brain_games.core import get_scenario
from brain_games.games.progression import get_exercise, task
"""
Модуль для запуска игры "Прогрессия".
"""


def main():
    """
    Запускаем игру "Прогрессия".
    """
    get_scenario(get_exercise, task)


if __name__ == "__main__":
    main()
