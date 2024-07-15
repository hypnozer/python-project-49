import random
import operator


task = "What is the result of the expression?"


def get_exercise():
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    type = random.choice(['+', '-', '*'])
    numbers = random.randint(1, 100), random.randint(1, 100)
    exercise = f"{numbers[0]} {type} {numbers[1]}"
    correct = str(action[type](*numbers))
    return exercise, correct
