from data import word_list
from user_interaction import guess
import random

print("Greetings to hangman")

CHOSEN_WORD = random.choice(word_list)
user_guess = guess()

print(user_guess)
word_dunder = ["_"] * len(CHOSEN_WORD)

for index, letter in enumerate(CHOSEN_WORD):
    if letter == user_guess:
        print("right")
        word_dunder[index] = letter
    else:
        print("wrong")

print("".join(word_dunder))
