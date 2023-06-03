import re
import random
from unidecode import unidecode
from src.data_list import word_list


CHOSEN_WORD = random.choice(word_list)
WORD_DUNDER_LIST = ["_"] * len(CHOSEN_WORD)
WORD_DUNDER_STR = "".join(WORD_DUNDER_LIST)


def guess_input():
    guess = input("Guess a letter: ").lower()

    if re.search(r"[\d+\-*/%&$#@!~^]", guess):
        raise ValueError("You can type only letter")

    if len(guess) == 0:
        raise ValueError("You must type a letter")

    if len(guess) > 1:
        raise ValueError("It is allowed only one letter per play")

    return guess


def letter_verification(user_choice):
    answer = ""
    for index, letter in enumerate(CHOSEN_WORD):
        if unidecode(letter) == unidecode(user_choice):
            WORD_DUNDER_LIST[index] = letter
            answer += "Right\n"
        else:
            answer += "Wrong\n"

    return answer
