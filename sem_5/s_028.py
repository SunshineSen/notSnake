''' Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы. 2 2    4 '''

def summa_a_b(a, b):
    if a == 0:
        return b
    return summa_a_b (a - 1, b + 1)

a = int (input ('Введите число а: '))
b = int (input ('Введите число b: '))
if a < 0 :
    print ('введите неотрицательное число')
elif b < 0:
   print ('введите неотрицательное число')   
else:
    print(summa_a_b(a, b))