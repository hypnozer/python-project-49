from brain_games.core import random_int
import operator
import random


TASK = "What is the result of the expression?"


def get_exercise():
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    type = random.choice(['+', '-', '*'])
    numbers = random_int(), random_int()
    exercise = f"{numbers[0]} {type} {numbers[1]}"
    correct = str(action[type](*numbers))
    return exercise, correct
