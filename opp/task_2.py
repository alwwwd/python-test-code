import random

class randomer:
    def rand_strings(self):
        pass
    def rand_bool(self):
        pass
    def rand_number(self):
        pass
    def rand_symbols(self):
        pass
    
class randomer_strings:
    list_of_leeters_up : str 
    list_of_leeters_low : str

    def __init__(self) :
        self.list_of_leeters_up = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.list_of_leeters_low = "qwertyuiopasdfghjklzxcvbnm"
    def rand_strings(self, up_or_low : str): 
        if up_or_low == "up": #  пареметры регистра: up,low
            return random.choice(self.list_of_leeters_up)
        
        return random.choice(self.list_of_leeters_low)
    

def set_class_method(random_params : randomer):
    if random_params ==  randomer_strings:
        print(randomer_strings.rand_strings("low"))

set_class_method(randomer_strings)
# randomer_strings.rand_strings(up_or_low = "up")