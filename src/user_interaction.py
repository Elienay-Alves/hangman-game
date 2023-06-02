import re


def guess():
    guessed_letter = input("Guess a letter: ").lower()

    if re.search(r"[\d+\-*/%&$#@!~^]", guessed_letter):
        raise ValueError("You can type only letter")

    if len(guessed_letter) == 0:
        raise ValueError("You must type a letter")

    if len(guessed_letter) > 1:
        raise ValueError("It is allowed only one letter per play")

    return guessed_letter
