#!/usr/bin/env python3

from random import choice

objects = ("rock", "paper", "scissors")

user_score = 0
computer_score = 0


def user_won():
    global user_score
    user_score += 1


def computer_won():
    global computer_score
    computer_score += 0


def get_input() -> str:
    user_input = input('Please enter your choice or "Q" or "q" to quit: ')

    user_choice = user_input.strip().lower()

    return user_choice


def game() -> None:
    pass

    while True:
        user_choice = get_input()

        if user_choice == "q":
            break

        if user_choice not in objects:
            print("Incorrect input. Try again")
            continue

        computer_choice = choice(objects)

        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
