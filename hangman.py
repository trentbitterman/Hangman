"""hangman.py - main file hangman"""

import initialize_game as ig
import finding_word as fw
import print_hangman as ph

def main():
    """
    main function for hangman.py:
    This function will hold all of the initialization
    code and the game loop
    """

    # Initialize all game data
    word_list, word_length = ig.initialize_game()



if __name__ == "__main__":
    main()
