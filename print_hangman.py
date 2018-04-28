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
    elif hangman_state == 6:
        print_state_six()
    elif hangman_state == 7:
        print_state_seven()
    elif hangman_state == 8:
        print_state_eight()
    elif hangman_state == 9:
        print_state_nine()
    else:
        print_state_ten()


def print_state_one():
    """Prints hangman with state one"""

    hangman = """
                _______
               |/      |
               |
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
               |
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
               |
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
               |       |
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
               |      \\|
               |
               |
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
               |
               |
               |
              _|___"""
    print(hangman)


def print_state_seven():
    """Prints hangman with state seven"""

    hangman = """
                _______
               |/      |
               |      (_)
               |      \\|/
               |       |
               |
               |
              _|___"""
    print(hangman)


def print_state_eight():
    """Prints hangman with state eight"""

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


def print_state_nine():
    """Prints hangman with state nine"""

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


def print_state_ten():
    """Prints hangman with state ten"""

    hangman = """
                _______
               |/      |
               |      (x_x)
               |      \\|/
               |       |
               |      / \\
               |
              _|___"""
    print(hangman)
