''' Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств. '''
elements_one = int (input ('введите количество элементов первого множества: '))
list_one = []
for i in range (elements_one):
    list_one.append (int (input ('введите элемент первого множества: ')))
set_one = set(list_one)
print (set_one)
elements_two = int (input ('введите количество элементов второго множества: '))
list_two = []
for i in range (elements_two):
    list_two.append (int (input ('введите элемент второго множества: ')))
set_two = set(list_two)
print (set_two)
sets_inter = list (set_one.intersection(set_two))
sets_inter.sort()
print ('в обоих наборах встречаются числа: ', sets_inter)