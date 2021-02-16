import json
import io
import os

class Parser():
    def __init__(self):
        self.directory = os.path.dirname(os.path.abspath(__file__))
        self.dump_words = os.path.join(directory, 'words.json')

    def parse_input(self, inp):
        with io.open(self.dump_words, 'r', encoding="utf8") as f:
            words = json.load(f)

        lowerinput = inp.lower()
        split_input = lowerinput.split(" ")
        for word in split_input:
            if word not in words:
                return word