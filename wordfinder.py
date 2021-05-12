"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """Creates a machine capable of reading in a list of words from a file 
    and then generateing random words from it"""
    def __init__(self, file):
        words_file =  open(file,"r")
        self.lst = self.fill(words_file)

        print (f"{len(self.lst)} words read")

    def random(self):
        return self.lst[randint(0,len(self.lst) - 1)]

    def fill(self, words_file):
        return [item.strip('\n') for item in words_file]

class SpecialWordFinder(WordFinder):
    """Creates a child of the original word finder that takes into acounnt empty inputs and #s"""
    def fill(self, words_file):
        return [item.strip() for item in words_file if item.strip() and not item.startswith("#")]
