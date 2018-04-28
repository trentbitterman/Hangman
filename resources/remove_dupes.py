#!/usr/bin/env python3

words = set()

word_file = open(
    "/Users/trentbitterman/python/hangman/resources/combined.txt", "r")

for word in word_file:
    words.add(word)

words = sorted(words)

word_file.close()

new_file = open(
    "/Users/trentbitterman/python/hangman/resources/combined.txt", "w")

for word in words:
    new_file.write("%s" % word)

new_file.close()
