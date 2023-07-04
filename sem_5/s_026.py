'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 '''

A = int (input("Введите число А: "))
B = int (input("Введите число В: "))

def degree(A, B):
    elem = 0
    if B == 1:
        return A
    else:
        elem = A*degree(A, B-1)
        return elem

print (f'{A} в степени {B} равно {degree(A, B)}')
