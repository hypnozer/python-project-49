import prompt


def scenario(get_exercise, task):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    attempt_count = 0

    print(task)

    while attempt_count <= 3:
        exercise, correct = get_exercise()
        print(f"Question: {exercise}")
        user_input = input("Your answer: ")
        if user_input == correct:
            print("Correct!")
            attempt_count += 1
        else:
            f"'{user_input}' is wrong answer ;(. Correct answer was {correct}.\
            \nLet.'s try again, {name}!"
            break
    print(f"Congratulations, {name}!")
