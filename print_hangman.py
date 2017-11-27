"""Functions to print out the state of the hanged man"""

def print_hangman(hangman_state):
    """Prints correct hangman depending on state"""

    if hangman_state == 1:
        print_state_one()
    elif hangman_state == 2:
        print_state_two()
    elif hangman_state == 3:
        print_state_three()
    elif hangman_state == 4:
        print_state_four()
    elif hangman_state == 5:
        print_state_five()
    else:
        print_state_six()

def print_state_one():
    """Prints hangman with state one"""

    hangman = """
                _______
               |/      |
               |      (_)
               |
               |
               |
               |
              _|___"""
    print(hangman)

def print_state_two():
    """Prints hangman with state two"""

    hangman = """
                _______
               |/      |
               |      (_)
               |       |
               |
               |
               |
              _|___"""
    print(hangman)

def print_state_three():
    """Prints hangman with state three"""

    hangman = """
                _______
               |/      |
               |      (_)
               |      \\|
               |
               |
               |
              _|___"""
    print(hangman)

def print_state_four():
    """Prints hangman with state four"""

    hangman = """
                _______
               |/      |
               |      (_)
               |      \\|/
               |
               |
               |
              _|___"""
    print(hangman)

def print_state_five():
    """Prints hangman with state five"""

    hangman = """
                _______
               |/      |
               |      (_)
               |      \\|/
               |       |
               |      /
               |
              _|___"""
    print(hangman)

def print_state_six():
    """Prints hangman with state six"""

    hangman = """
                _______
               |/      |
               |      (_)
               |      \\|/
               |       |
               |      / \\
               |
              _|___"""
    print(hangman)
