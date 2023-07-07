''' Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] (диапазон 5 10)
Вывод: [1, 9, 13, 14, 19] '''

list_one = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print (list_one)

list_two = []

min_number = int ( input('Введите начальное число диапазона: '))
max_number = int ( input('Введите конечное число диапазона: '))

def index_of_elements (min_number, max_number):
    list_one = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    for i in range(len(list_one)):
        if min_number <= list_one[i] <= max_number:
            list_two.append(i)
    return (list_two)

print ('индексы в заданном диапазоне: ', index_of_elements (min_number, max_number))