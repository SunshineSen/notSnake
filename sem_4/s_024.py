''' В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки. '''

number_of_bushes = int (input ('введите количество кустов на грядке '))
number_of_berries = []
picked_berries = []
for i in range (number_of_bushes):
    number_of_berries.append (int (input ('введите элемент первого множества: ')))

for i in range(number_of_bushes):
    if i == 0:
        picked_berries.append(number_of_berries[-1] + number_of_berries[i] + number_of_berries[i+1])
    elif i in range (1, number_of_bushes-1):
        picked_berries.append(number_of_berries[i-1] + number_of_berries[i] + number_of_berries[i+1])
    elif i == number_of_bushes-1:
        picked_berries.append(number_of_berries[0] + number_of_berries[number_of_bushes-2] + number_of_berries[number_of_bushes-1])

print ('максимальное число ягод - ', max(picked_berries), 'будет собрано с куста ', picked_berries.index(max(picked_berries))+1)