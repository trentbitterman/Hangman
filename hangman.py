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

    # Get the game difficulty from player
    game_difficulty = ig.get_game_difficulty()

    # Load correct game file
    filename = ig.get_game_file(game_difficulty)

    # Initialize word_list
    word_list = ig.initialize_word_list(filename)

    # Get word length from player
    word_length = ig.get_word_length()

    # Cull words of the wrong length from word_list
    fw.narrow_by_length(word_list, word_length)



if __name__ == "__main__":
    main()
