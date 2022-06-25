import random


class Randomer:
    def random(self):
        pass

class RandomerBool(Randomer):
    def random(self):
       return bool(int(random.random() * 10) % 2 )
    

class RandomerIntengers(Randomer):
    left_value : int 
    right_value : int 
    number_of_ditgits : int

    def __init__(self,left_value, right_value):
        self.right_value = right_value
        self.left_value = left_value
        self.number_of_ditgits = self.find_number_of_ditgits()

    def find_number_of_ditgits(self):
        number = abs(self.right_value)
        counter = 0
        while number != 0:
            number //= 10
            counter += 1
        return counter

    def random(self):
        return (int(random.random() * 10 ** self.number_of_ditgits) %
                (self.right_value + 1 - self.left_value) + self.left_value)




class RandomerLetters(Randomer):
    list_of_letters_up : str 
    list_of_letters_low : str
    is_upper_case : bool 
    
    def __init__(self, is_upper_case : bool):
        self.is_upper_case = is_upper_case
        self.list_of_letters_low = "qwertyuiopasdfghjklzxcvbnm"
        self.list_of_letters_up = "QWERTYUIOPASDFGHJKLZXCVBNM"

    def change_case(self, new_case : bool):
        self.is_upper_case = new_case

    def random(self): 
        index = int(random.random() * 100) % len(self.list_of_letters_low) 

        if self.is_upper_case: 
            return self.list_of_letters_up[index]
       
        return self.list_of_letters_low[index]
        



class RandomerStrings(Randomer):
    # комозиция - когда полем одного класса является объект другово класса 
    letters_generater : RandomerLetters
    string_length : int 

    def __init__(self, is_upper_case : bool, string_length : int):
        self.letters_generater = RandomerLetters(is_upper_case)
        self.string_length = string_length

    def change_case(self, new_case : bool):
        self.letters_generater.change_case(new_case)

    def random(self): 
        res_string = ""
        for i in range(self.string_length):
            res_string += self.letters_generater.random()
        return res_string

    def change_string_legth(self, new_length):
        self.string_length = new_length


def call_random(random_generator : Randomer):
    print(random_generator.random())

strings = RandomerStrings(False, 100)
letters = RandomerLetters(False)
bool_data = RandomerBool()
intengers = RandomerIntengers(-3,-1)

call_random(strings)
call_random(letters)
call_random(bool_data)
call_random(intengers)

