from brain_games.core import random_int
import math


task = "Find the greatest common divisor of given numbers."


def get_exercise():
    numbers = random_int(), random_int()
    exercise = f"{numbers[0]} {numbers[1]}"
    correct = str(math.gcd(numbers[0], numbers[1]))
    return exercise, correct
