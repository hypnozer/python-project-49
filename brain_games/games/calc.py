import random
import operator


task = "What is the result of the expression?"


def run_exercise():
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    type = random.choice(list(action))
    numbers = random.randint(1, 999), random.randint(1, 999)
    exercise = type, numbers
    correct = action[type](numbers)
    return exercise, correct
