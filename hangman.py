"""hangman.py - main file hangman"""

import initialize_game as ig
import finding_word as fw

def main():
    """
    main function for hangman.py:
    This function will hold all of the initialization
    code and the game loop
    """

    # Greet the player
    print("Welcome to Hangman!")

    # Initialize word_list
    word_list = ig.initialize_word_list()

    # Get word length from player
    word_length = ig.get_word_length()

    # Cull words of the wrong length from word_list
    print(len(word_list))
    fw.narrow_by_length(word_list, word_length)
    print(len(word_list))



if __name__ == "__main__":
    main()
