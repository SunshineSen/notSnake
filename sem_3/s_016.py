''' Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''
elements = int (input ('введите число элементов в массиве: '))
my_list = []
for i in range(elements):
    my_list.append(int(input ('элемент массива: ')))
print(my_list)
number = int (input ('введите проверяемое число: '))
count = 0
for i in range (elements):
    if number == my_list[i]:
        count += 1
print ('число', number, 'повторяется', count, 'раз')