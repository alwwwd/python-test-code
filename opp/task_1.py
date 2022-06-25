class Cube:
    height : int 
    length : int
    width :  int 
    
    def __init__(self, size): # в cube_h_l_w хранится длинна, ширина и высота: она  одна       
        self.height = size
        self.length = size
        self.width = size


    def change_size_by_number(self, number_for_up):
        self.height *= number_for_up
        self.length *= number_for_up
        self.width *= number_for_up

    def reset_size(self):
        self.height = 0
        self.length = 0
        self.width = 0

    def get_surface_square(self):
        H = self.height ** 2 * 6
        return H

    def get_volume(self):
        result = self.height * self.length * self.width
        
        return result

    def print_info(self):
        print(f"cube height is {self.height}")
        print(f"cube length is {self.length}")
        print(f"cube width is {self.width}")

first_cube = Cube(2000)
res = first_cube.get_volume()

print(f"cube volume result is {res}")

first_cube.print_info()

cube_square_res = first_cube.get_surface_square()

print(cube_square_res)