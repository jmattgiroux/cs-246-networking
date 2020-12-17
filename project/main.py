import random


class Translator:
    dogWord = ["BORK", "baRK", "ArF", "ruff"]

    # https://www.w3schools.com/python/python_lists.asp
    def __init__(self):
        self.stringToTranslate = " "
        self.translatedString = ""
        self.randomNumber = 1


    def translate_to_dog(self):
        # Reset our translation
        self.translatedString = ""
        # https://www.w3schools.com/python/python_for_loops.asp
        # https://www.geeksforgeeks.org/python-string-count/
        for x in range(self.stringToTranslate.count(" ") + 1):
            self.translatedString = self.translatedString + self.get_dog_word(self) + " "

    def set_string(self, string):
        self.stringToTranslate = string

    def get_string(self):
        return self.stringToTranslate

    def get_dog_string(self):
        self.translate_to_dog(self)
        return self.translatedString

    def update_number(self):
        # https://www.geeksforgeeks.org/random-numbers-in-python/
        self.randomNumber = random.choice([0, 1, 2, 3])

    def get_dog_word(self):
        self.update_number(self)
        return self.dogWord[self.randomNumber]


if __name__ == '__main__':

    translator = Translator

    # https://www.askpython.com/python/examples/python-user-input
    translator.set_string(translator, input("Please enter the text you would like to translate to dog-ish: "))

    print(translator.get_dog_string(translator))

