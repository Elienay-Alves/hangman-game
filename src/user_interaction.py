import re


def guess():
    guessed_letter = input("Guess a letter: ")

    if re.search(r"[\d+\-*/%&$#@!~^]", guessed_letter):
        raise ValueError("You must type a letter")

    if len(guessed_letter) == 0:
        raise ValueError("You must type a letter")

    return guessed_letter
