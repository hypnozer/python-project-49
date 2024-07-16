import prompt
import random


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def congratulate_user(name):
    print(f"Congratulations, {name}!")


def get_scenario(get_exercise, task):
    name = welcome_user()
    print(task)

    for _ in range(3):
        exercise, correct = get_exercise()
        print(f"Question: {exercise}")
        try_ = input("Your answer: ")

        if try_ != correct:
            print(
                f"'{try_}' is wrong answer ;(. Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    congratulate_user(name)


def is_prime(num):
    i = 2
    while num % i != 0:
        i += 1
    return i == num


def is_even(value):
    return value % 2 == 0


def random_int():
    return random.randint(1, 100)
