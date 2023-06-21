''' По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всехчисел от 1 до N) 0! = 1 Решить задачу используя цикл while
Input: 5
Output: 120 '''

N = int(input ('введите значение N '))
count = 1
factorial = 1
while count <= N:
    factorial = factorial*count
    count += 1
print (factorial)