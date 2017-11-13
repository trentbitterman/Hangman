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

    print("Would you like to play the game at easy, medium, or hard?")
    print("Note: Playing the game at hard will heavily slow things down.")

    # Ask player for game difficulty
    game_difficulty = None
    while game_difficulty is None:
        try:
            game_difficulty = input().lower()
            if game_difficulty == "easy" or game_difficulty == "e":
                game_difficulty = "e"
                break
            elif game_difficulty == "medium" or game_difficulty == "m":
                game_difficulty = "m"
                break
            elif game_difficulty == "hard" or game_difficulty == "h":
                game_difficulty = "h"
                break
            game_difficulty = None
            print("Try inputting \"easy\" or \"e\"")
        except ValueError:
            print("Try inputting \"easy\" or \"e\"")
    return game_difficulty

def get_game_file(game_difficulty, word_length):
    """Returns appropriate filename for set difficulty"""

    if game_difficulty == "h":
        return "resources/hard_lists/" + str(word_length) + "-words.txt"
    elif game_difficulty == "m":
        return "resources/medium_lists/" + str(word_length) + "-words.txt"
    return "resources/easy_lists/" + str(word_length) + "-words.txt"

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

    # Get the game difficulty from player
    game_difficulty = get_game_difficulty()

    # Get word length from player
    word_length = get_word_length()

    # Load correct game file
    filename = get_game_file(game_difficulty, word_length)

    # Initialize word_list
    word_list = initialize_word_list(filename)

    return word_list, word_length
