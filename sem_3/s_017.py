''' Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6 '''
N = int (input ('Введите число элементов в массиве: ' ))
list_one = []
for i in range(N):
    list_one.append(input('элемент массива: '))
print(list_one)
list_two = []
for elem in list_one:
    if elem not in list_two:
        list_two.append(elem)
print(len(list_two), list_two)