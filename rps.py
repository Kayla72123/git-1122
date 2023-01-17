#!/usr/bin/env python3

from random import choice

objects = ("rock", "paper", "scissors")


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
