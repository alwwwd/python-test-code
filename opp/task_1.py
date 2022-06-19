class cube:
    cube_height : int 
    cube_length : int
    cube_width :  int 
    
    def __init__(self, cube_h_l_w): # в cube_h_l_w хранится длинна, ширина и высота: она  одна       
        self.cube_height = cube_h_l_w
        self.cube_length = cube_h_l_w
        self.cube_width = cube_h_l_w
    
    def upper_cube(self, number_for_up):
        self.cube_height += number_for_up
        self.cube_length += number_for_up
        self.cube_width += number_for_up

    def reset_cube_params(self):
        self.cube_height = 0
        self.cube_length = 0
        self.cube_width = 0

    def in_cube_square_res(self):
        H = self.cube_height ** 2  * 6
        return H

    def cube_volume(self):
        result = self.cube_height * self.cube_length * self.cube_width
        
        return result

    def all_about_cube(self):
        print(f"cube height is {self.cube_height}")
        print(f"cube length is {self.cube_length}")
        print(f"cube width is {self.cube_width}")

first_cube = cube(10)
res = first_cube.cube_volume()

print(f"cube volume result is {res}")

first_cube.all_about_cube()

cube_square_res = first_cube.in_cube_square_res()

print(cube_square_res)