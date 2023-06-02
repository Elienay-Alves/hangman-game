def guess():
    guessed_letter = input("Guess a letter: ")

    if len(guessed_letter) == 0:
        raise ValueError("You must type a letter")
    return guessed_letter
