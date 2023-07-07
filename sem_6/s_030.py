''' Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки
Ввод: 7 2 5
Вывод: 7 9 11 13 15 '''

first_number = int (input ('Введите первое число прогрессии: '))
step = int (input ('Введите шаг прогрессии: '))
numb_of_elements = int (input  ('Введите количество элементов прогрессии: '))

progression = []
def arithm_progres (a, b, c):
    for i in range (c):
        progression.append(a+i*b)
    return progression
print (arithm_progres(first_number, step, numb_of_elements))
