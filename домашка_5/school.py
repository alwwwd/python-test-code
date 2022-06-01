# Реализовать приложение "Электронный журнал". В электронном журнале должна хранится информация об учениках: ФИО, класс, средний балл по математике, средний балл по русскому языку. Во время работы программы данные об учениках должны загружаться из файла, если он не пустой. Программа должна хранить данные об учениках в списке, а по завершении программы должна осуществляться выгрузка в файл всей информации о школьниках.
# Реализовать следующие функции:
# 1) добавления нового ученика 
# 2) удаление ученика из базы
# 3) просмотр списка учеников с возможностью сортировки по какому-то полю (фамилия, имя, отчество, класс или средний балл) (по умолчанию сортировать по фамилии)
# 4) подсчет среднего балла по классу (нужно передавать наименование класса, для подсчета нужных значений) (по умолчанию средний балл считается по школе)
def add_people(people_name,grade=1,third_bal_ru=100,third_bal_math=100):
    file.seek(0)
    people_add =[people_name, grade, third_bal_ru, third_bal_math]
    file.write(str(f"\n{people_add}"))
    print(f"{people_name} is added, {people_name} in {grade} ")


def delete_people(people_name,grade=1):
    file = open("/Users/alex/Desktop/test-python/домашка_5/school.txt", "w")
    file.seek(0)
    people_remove = [people_name, grade]
    file.readline().replace(people_name,"")
    file.readline().replace(grade,"")
    print(f"{people_name} is deleted") 

def see_and_sort(grade):
    pass

def third():
    pass


# init 
file = open("/Users/alex/Desktop/test-python/домашка_5/school.txt", "a")
frist_action =  "1)добавления нового ученика\n"
second_action = "2)удаление ученика из базы\n"
third_action = "3)просмотр списка учеников с возможностью сортировки по какому-то полю (фамилия, имя, отчество, класс или средний балл) (по умолчанию сортировать по фамилии)\n"
fourth_action = "4)подсчет среднего балла по классу \n(нужно передавать наименование класса, для подсчета нужных значений) (по умолчанию средний балл считается по школе)\n"
print(f"выберите режим работы программы:\n \n{frist_action}{second_action}{third_action}{fourth_action}")

print(delete_people("ass",grade=5))
