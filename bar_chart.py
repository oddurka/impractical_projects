"""Counts the number of occurances of a letter in given sentence and displays them in a bar chart"""
from pprint import pprint
from collections import defaultdict

def bar_chart(sentence):
    chart = dict()
    for letter in sentence.replace(" ","").lower():
        if letter in chart:
            bar = chart[letter]
            bar.append(letter)
            chart[letter] = bar
        elif letter not in chart:
            chart[letter] = [letter]
    pprint(chart)


def book_solution(sentence):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    mapped = defaultdict(list)
    for character in sentence:
        character = character.lower()
        if character in ALPHABET:
            mapped[character].append(character)
    pprint(mapped, width=110)

sentence = "The quick brown fox jumps over the lazy dog"
sentence_2 = "Like the castle in its corner in a medieval game, I foresee terrible trouble and I stay just the same."
book_solution(sentence)
