''' Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. П
ользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X '''

'''elements = int (input ('введите число элементов в массиве: '))
list_one = []
for i in range (elements):
    list_one.append (int (input ('элемент массива: ')))
print(list_one) '''

# другой вариант ввода
elements = int (input ('введите число элементов в массиве: '))
string = input ("введите через пробел список элементов: ")
list_one = [ int(i) for i in string.split() ]
number = int (input ('введите число: '))
list_two = []
for i in range (elements):
    list_two.append (abs (number - list_one[i]))

min_ind = list_two.index(min(list_two))
print ('наиболее близкое к числу', number, '- число', list_one[min_ind])