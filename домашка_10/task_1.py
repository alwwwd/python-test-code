from opcode import stack_effect
from webbrowser import get


class stack:
    max_len : int
    stack_list = []    

    def __init__(self, max_len):
        self.max_len = max_len  
        self.stack_list = []
    
    def count(self):
        counter = 0 
        for i in range(len(self.stack_list)):
            if i != len(self.stack_list):
                counter += 1
            elif self.stack_list > self.max_len:
                print("Stack length exceeded maximum_number of stack elements, please increase stack length or increase stack length of stack elements")

        return counter    

    def get_element_by_index(self, index : int = 0):
       return(self.stack_list[index])
       print(stack_list)

    def append(self, element):
        if len(self.stack_list) >= self.max_len:
            print("stack is full, please increase")
        else:
            self.stack_list += [element]
            return self.stack_list

    def append_left(self, element):
        backup_list = self.stack_list
        self.stack_list = None
        self.stack_list = [element]
        self.stack_list += backup_list

        return self.stack_list

    def pop(self,element_id : int = -1):
        bakcup = self.stack_list[0:element_id]
        self.stack_list = bakcup
        return self.stack_list 
    
    def pop_left(self, element_id : int = -2):
        bakcup = self.stack_list[0:element_id]
        self.stack_list = bakcup
        return self.stack_list
    
    # pleas print info about self.stack_list
    def print_info(self):
        return self.stack_list

my_stack = stack(10)

# mystac.append("hi")
my_stack.append("hi")
my_stack.append("hdj")
my_stack.append("s9x")
my_stack.append("ds")
my_stack.append("ru")




my_stack.pop_left(-2)
print(my_stack.append("en"))

my_stack.get_element_by_index()

