import random
import operator


task = "What is the result of the expression?"


def get_action(type, *args):
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    return action[type](*args)


def get_exercise():
    type = random.choice(['+', '-', '*'])
    numbers = random.randint(1, 999), random.randint(1, 999)
    exercise = f"{numbers[0]} {type} {numbers[1]}"
    correct = get_action(type, numbers)
    return exercise, correct
