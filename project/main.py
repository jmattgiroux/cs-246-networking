
class Translator:

    def __init__(self):
        self.stringToTranslate = " "

    def translate_to_dog(self):
        pass

    def set_string(self, string):
        self.stringToTranslate = string

    def get_string(self):
        return self.stringToTranslate


if __name__ == '__main__':

    translator = Translator

    # https://www.askpython.com/python/examples/python-user-input
    translator.set_string(translator, input("Please enter the text you would like to translate to dog-ish: "))

    print(translator.get_string(translator))

