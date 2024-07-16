import random


task = "What number is missing in the progression?"


def get_exercise():
    first_elem = random.randint(1, 100)
    diff = random.randint(2, 10)
    exercise = [first_elem + i * diff for i in range(random.randint(5, 11))]
    index = random.randint(0, len(exercise) - 1)
    correct = str(exercise[index])
    exercise[index] = ".."
    return ' '.join([str(item) for item in exercise]), correct
