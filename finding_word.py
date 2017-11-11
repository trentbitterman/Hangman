"""finding_word.py - functions to narrow down word_list"""

def narrow_by_length(word_list, word_length):
    """
    narrows down word list by removing words
    of the wrong length
    """

    for word in word_list[:]:
        if not len(word) == word_length:
            word_list.remove(word)
