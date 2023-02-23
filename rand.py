import random

class Encoder:
    def __init__(self, number):
        self.__number = number

    def __encode(self):
       return self.__number * random.randint(1, 10)

    def show(self):
        print(self.__encode())

number = 42
encoder = Encoder(number)
encoder.show()