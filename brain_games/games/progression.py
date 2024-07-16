import random
from brain_games.core import random_int


TASK = "What number is missing in the progression?"


def get_exercise():
    first_elem = random_int()
    diff = random.randint(2, 10)
    exercise = [first_elem + i * diff for i in range(random.randint(5, 11))]
    index = random.randint(0, len(exercise) - 1)
    correct = str(exercise[index])
    exercise[index] = ".."
    return ' '.join([str(item) for item in exercise]), correct
