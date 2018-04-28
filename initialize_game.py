"""initialize_game.py - functions for setting up game state"""

import lzma


def get_word_length():
    """Gets the length of the word from the player"""

    # Get game information from player
    print("How long is your word?")

    # Safely get an int from the player
    word_length = None
    while word_length is None:
        try:
            word_length = int(input())
        except ValueError:
            print("Sorry, you have to enter an integer, e.g. \"5\"")

    return word_length


def initialize_word_list(filename):
    """Initializes word list"""

    # Get word_file
    try:
        word_file = lzma.open(filename, mode="rt")
    except FileNotFoundError:
        print("Error: " + filename + " not found.")

    word_list = []

    # Iterate over word_file and build list
    for word in word_file:
        word_list.append(word.strip().lower())

    word_file.close()

    return word_list


def get_game_file(word_length):
    """Returns appropriate filename for set difficulty"""
    return "resources/word_lists/" + str(word_length) + "-words.txt.xz"


def initialize_game():
    """Uses above functions to initialize all game data"""

    hangman_art = """
                   _
                  | |
                  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
                  | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
                  | | | | (_| | | | | (_| | | | | | | (_| | | | |
                  |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                                      __/ |
                                     |___/
                  """

    # Greet the player
    print(hangman_art)

    # Get word length from player
    word_length = get_word_length()

    # Load correct game file
    filename = get_game_file(word_length)

    # Initialize word_list
    word_list = initialize_word_list(filename)

    return word_list
