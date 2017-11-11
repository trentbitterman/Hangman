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

def initialize_word_list(filename):
    """Initializes word list"""

    # Get word_file
    try:
        word_file = open(filename, "r")
    except FileNotFoundError:
        print("Error: " + filename + " not found.")

    word_list = []

    # Iterate over word_file and build list
    for word in word_file:
        word_list.append(word.strip())

    word_file.close()

    return word_list

def get_game_difficulty():
    """Lets player select game difficulty"""

    print(
        """
        Would you like to play the game at easy, medium, or hard?
        Note: Playing the game at hard will heavily slow things down.
        """)

    # Ask player for game difficulty
    game_difficulty = None
    while game_difficulty is not ("easy" or "e" or "medium" or "m" or "hard" or "h"):
        try:
            game_difficulty = input().lower()
        except ValueError:
            print("Try inputting \"easy\" or \"e\"")

    return game_difficulty

def get_game_file(game_difficulty):
    """Returns appropriate filename for set difficulty"""

    if game_difficulty == "hard" or "h":
        return "resources/word_list_large.txt"
    elif game_difficulty == "medium" or "m":
        return "resources/word_list_medium.txt"
    return "resources/word_list_small.txt"
