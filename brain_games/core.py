import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def congratulate_user(name):
    print(f"Congratulations, {name}!")


def get_brain_game(get_exercise, task):
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
