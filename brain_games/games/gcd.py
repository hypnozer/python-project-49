import random
import math


task = "Find the greatest common divisor of given numbers."


def get_exercise():
    numbers = random.randint(1, 999), random.randint(1, 999)
    exercise = f"{numbers[0]} {numbers[1]}"
    correct = str(math.gcd(numbers[0], numbers[1]))
    return exercise, correct
