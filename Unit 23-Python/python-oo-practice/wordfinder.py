"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    def __init__(self, path):
        self.path = path

        with open(path) as file: 
            self.contents = file.readlines()
            print(f"{len(self.contents)} words read.")

    def random(self):
        print(random.choice(self.contents))

word_finder = WordFinder('words.txt')

word_finder.random()
