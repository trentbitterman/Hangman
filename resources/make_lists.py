word_file = open(
    "/Users/trentbitterman/python/hangman/resources/all_words.txt", "r")

word_list = []

for word in word_file:
    word_list.append(word.strip())
word_file.close()

for i in range(1, 100):
    small_list = [word for word in word_list if len(word) == i]
    if not len(small_list) is 0:
        filename = "/Users/trentbitterman/python/hangman/resources/word_lists/" + \
            str(i) + "-words.txt"
        new_file = open(filename, "w")
        for word in small_list:
            new_file.write("%s\n" % word)
        new_file.close()
