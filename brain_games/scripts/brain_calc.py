import random
import prompt


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


#!usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.games.even import get_question_and_answer, MANUAL


def main():
    run_game(get_question_and_answer, MANUAL)


if __name__ == "__main__":
    main()
