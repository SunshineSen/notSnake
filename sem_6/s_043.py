'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
ввод 12323
вывод 2 '''

a = [1, 2, 3, 1, 5]
count = 0
for i in range(len(a) - 1):
    for j in range(i + 1 , len(a)):
        if a[i] == a[j]:
            count += 1
print (count)