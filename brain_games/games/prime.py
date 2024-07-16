from brain_games.core import is_prime, random_int


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_exercise():
    exercise = random_int()
    if is_prime(exercise):
        correct = 'yes'
    else:
        correct = 'no'
    return exercise, correct
