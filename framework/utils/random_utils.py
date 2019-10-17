import random

characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"


class RandomUtils:
    @staticmethod
    def get_random_string():
        random_string = ""
        for i in range(10):
            random_string += random.choice(characters)
        return random_string
