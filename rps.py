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
    # TODO Exercise 2: Your code here
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
            # TODO Exercise 3: Your code here
            break

        if user_choice not in objects:
            print("Incorrect input. Try again")
            continue

        computer_choice = choice(objects)

        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        if user_choice == computer_choice:
            print("Draw.")
        elif user_choice == "rock" and computer_choice == "scissors":
            user_won()
            print("You won")
        elif user_choice == "paper" and computer_choice == "rock":
            user_won()
            print("You won")
        elif user_choice == "scissors" and computer_choice == "paper":
            user_won()
            print("You won")
        else:
            computer_won()
            print("Computer won")

        print(f"Score is {user_score}-{computer_score}")


def main() -> None:
    game()


if __name__ == "__main__":
    main()
