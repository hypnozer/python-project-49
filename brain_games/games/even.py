from brain_games.core import random_int

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    return value % 2 == 0


def get_exercise():
    exercise = random_int()
    if is_even(exercise):
        correct = 'yes'
    else:
        correct = 'no'
    return exercise, correct
