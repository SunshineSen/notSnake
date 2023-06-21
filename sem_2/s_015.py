''' Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9 '''
n = int(input('количество арбузов: '))
min_weight=10**100
max_weight = 0
for i in range(n):
    weight = int(input ('масса арбуза: '))
    if weight < min_weight:
        min_weight = weight
    if weight > max_weight:
        max_weight = weight
print( min_weight, max_weight)
