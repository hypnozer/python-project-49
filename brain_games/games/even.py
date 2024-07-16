from brain_games.core import is_even, random_int

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_exercise():
    exercise = random_int()
    if is_even(exercise):
        correct = 'yes'
    else:
        correct = 'no'
    return exercise, correct
