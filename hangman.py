#!/usr/bin/env python3
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

    game_finished = False
    guess_letter = "e"
    hangman_state = 0
    guessed_letters = ["e"]

    # Initialize all game data
    word_list = ig.initialize_game()

    while not game_finished:
        # Computer makes guess (first guess always 'e')
        fw.make_guess(guess_letter)
        answer = fw.get_answer()
        if answer:
            guess_string = fw.get_guess_string()
            positions = fw.get_location(guess_string, guess_letter)
            word_list = fw.cull_word_list_by_position(word_list, positions, guess_letter)
        else:
            hangman_state += 1
            ph.print_hangman(hangman_state)
            word_list = fw.cull_word_list_by_letter(word_list, guess_letter)

        if hangman_state == 6:
            print("Congratulations, you beat me!")
            game_finished = True
            break

        if len(word_list) == 1:
            print("I think that the word is " + word_list[0] + ". Is that correct?")
            user_answer = None
            while user_answer is None:
                try:
                    user_answer = input().lower()
                    if user_answer[0] == "y":
                        print("Haha, I won!")
                        game_finished = True
                        break
                except ValueError:
                    print("Try yes or no")
            else:
                print("Congratulations, you beat me!")
                game_finished = True

        if word_list == []:
            print("Congratulations, you beat me!")
            game_finished = True

        guess_letter, guessed_letters = fw.make_new_guess(word_list, guessed_letters)






if __name__ == "__main__":
    main()
