'''Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2'''

n = int (input ('введите число дней: '))
current_count = 0
max_count = 0
for i in range(n):
    temp = int(input('температура: '))
    if temp > 0:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
        current_count = 0
print(max_count)
