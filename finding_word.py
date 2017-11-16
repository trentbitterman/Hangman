"""finding_word.py - functions to narrow down word_list"""

def make_guess(letter):
    """Function that tells the player the computer's guess"""

    print("My guess is " + str(letter))

def get_answer():
    """Determines whether the guess was correct"""

    print("Was my guess correct? Yes or no.")

    answer = None
    while answer is None:
        try:
            answer = input().lower()
        except ValueError:
            print("Try yes or no")
    if answer[0] == "y":
        return True
    return False

def get_guess_string():
    """Gets the word with all guessed letters"""

    print("Where is the letter? Input all the guessed letters with \"-\" in between.")
    answer = None
    while answer is None:
        try:
            answer = input().lower()
        except ValueError:
            print("Your input should be similar to this: \"-a-gma-\" for the word hangman.")
    return answer

def get_location(guess_string, guess_letter):
    """Determines where guess_letter is in guess_string"""

    positions = []

    for position, letter in enumerate(guess_string):
        if letter == guess_letter:
            positions.append(position)
    return positions

def cull_word_list_by_position(word_list, positions, guess_letter):
    """Removes words that don't contain the guessed letter in the correct location"""

    bad_list = set()
    word_list = set(word_list)

    for word in word_list:
        for position in positions:
            if word[position] != guess_letter:
                if word not in bad_list:
                    bad_list.add(word)

    good_list = list(word_list.difference(bad_list))

    return good_list

def cull_word_list_by_letter(word_list, guess_letter):
    """Removes words that contain the guessed letter"""

    new_list = []
    for word in word_list:
        if guess_letter not in word:
            new_list.append(word)
    return new_list

def make_new_guess(word_list, guessed_letters):
    """Make new guess depending on frequency of letters"""

    letters = {}
    for word in word_list:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

    max_amount = -1
    final_letter = ""
    for letter, amount in letters.items():
        if (amount > max_amount) and (letter not in guessed_letters):
            final_letter = letter
            max_amount = amount
    guessed_letters.append(final_letter)
    return final_letter, guessed_letters
