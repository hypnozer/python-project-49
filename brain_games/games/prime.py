import random
import math


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 2
    while num % i != 0:
        i += 1
    return i == num


def get_exercise():
    exercise = random.randint(1, 100)
    if is_prime(exercise):
        correct = 'yes'
    else:
        correct = 'no'
    return exercise, correct
