from data import word_list
from user_interaction import guess
import random

print("Greetings to hangman")

CHOSEN_WORD = random.choice(word_list)
user_guess = guess()

print(user_guess)
for letter in CHOSEN_WORD:
    if letter == user_guess:
        print("right")
    else:
        print("wrong")
