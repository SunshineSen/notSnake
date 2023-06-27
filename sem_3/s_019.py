''' Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3] '''
list_one = [1, 2, 3, 4, 5]
sdvig = 3
for i in range(sdvig):
    last = list_one.pop()
    list_one.insert(0, last)
print (list_one)

#через срез
list_1 = [1, 2, 3, 4, 5]
k = 3
list_2 = list_1[k:] + list_1[:k]
print (list_2)