import random
import numpy as np # поддержка pip3.10(pip3.9 тупит)  и ниже: pip3.10 install numpy

class randomer:
    def random(self):
        pass

class randomer_bool(randomer):
    def random(self):
        return bool(np.random.randint(2, size=1))

bool = randomer.bool()

class randomer_letters(randomer):
    list_of_leeters_up : str 
    list_of_leeters_low : str

    def random(self, up_or_low : str = "low"): 
        self.list_of_leeters_up = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.list_of_leeters_low = "qwertyuiopasdfghjklzxcvbnm"

        if up_or_low == "up": #  пареметры регистра: up,low
            return random.choice(self.list_of_leeters_up)

        return random.choice(self.list_of_leeters_low)

letters = randomer_letters()

class randomer_strings(randomer):
    list_of_leeters_up : str 
    list_of_leeters_low : str

    def __init__(self, list_of_leeters_low : str, list_of_leeters_up : str):
        super().__init__(list_of_leeters_low, list_of_leeters_up)

    def random(self, up_or_low : str = "low"): 
        self.list_of_leeters_up = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.list_of_leeters_low = "qwertyuiopasdfghjklzxcvbnm"

        if up_or_low == "up": #  пареметры регистра: up,low
            return random.choice(self.list_of_leeters_up)

        return random.choice(self.list_of_leeters_low)

strings = randomer_strings()

