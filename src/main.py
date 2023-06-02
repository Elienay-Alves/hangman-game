from data import word_list
from user_interaction import guess
from unidecode import unidecode
import random

print("Greetings to hangman")

CHOSEN_WORD = random.choice(word_list)
user_guess = guess()

print(CHOSEN_WORD)
word_dunder = ["_"] * len(CHOSEN_WORD)

for index, letter in enumerate(CHOSEN_WORD):
    if unidecode(letter) == unidecode(user_guess):
        print("right")
        word_dunder[index] = letter
    else:
        print("wrong")

print("".join(word_dunder))
