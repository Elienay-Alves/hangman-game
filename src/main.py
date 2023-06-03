import user_interaction

WELCOME_MESSAGE = "Greetings to hangman"

if __name__ == "__main__":
    print(WELCOME_MESSAGE)
    print(user_interaction.letter_verification(user_interaction.guess_input()))
    print(user_interaction.WORD_DUNDER_STR)
    print(user_interaction.CHOSEN_WORD)
