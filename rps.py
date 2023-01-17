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


def main() -> None:
    pass


if __name__ == "__main__":
    main()
