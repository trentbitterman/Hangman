"""initialize_game.py - functions for setting up game state"""

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

def initialize_word_list():
    """Initializes word list"""

    # Get word_file
    word_file = open("test.txt", "r")

    word_list = []

    # Iterate over word_file and build list
    for word in word_file:
        word_list.append(word.strip())

    return word_list
