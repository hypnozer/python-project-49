import random
import prompt


def is_even(value):
    if value % 2 != 0:
        return "no"
    else:
        return "yes"


def main():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    first, second, third = (
        random.randint(1, 999),
        random.randint(1, 999),
        random.randint(1, 999),
    )
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f"Question: {first}")
    user_input = input("Your answer: ")
    if user_input == is_even(first):
        print("Correct!")
        print(f"Question: {second}")
        user_input = input("Your answer: ")
        if user_input == is_even(second):
            print("Correct!")
            print(f"Question: {third}")
            user_input = input("Your answer: ")
            if user_input == is_even(third):
                print(f"Congratulations, {name}!")
            else:
                print(
                    f"'{user_input}' is wrong answer ;(. Correct answer was \
                        {is_even(third)}.\nLet.'s try again, {name}!"
                )
        else:
            print(
                f"'{user_input}' is wrong answer ;(. Correct answer was \
                    {is_even(second)}.\nLet's try again, {name}!"
            )
    else:
        print(
            f"'{user_input}' is wrong answer ;(. Correct answer was \
                {is_even(first)}.\nLet's try again, {name}!"
        )


if __name__ == "__main__":
    main()
