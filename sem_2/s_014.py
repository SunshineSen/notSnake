''' Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''


''' N = int (input('введите ограничение N: '))
degree = 0
result = 0
while degree <= N:
    result = 2**degree
    print ('2 в сепени', degree, 'равно', result)
    degree += 1
'''
N = int (input('введите ограничение N: '))
degree = 0
result = 0
for degree in range(N+1):
    result = 2**degree
    print ('2 в сепени', degree, 'равно', result)
