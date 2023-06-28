''' Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. '''
''' string = 'a a a b c a a d c d d'.replace(' ', '') # replace - замена что на что
answer = ''
for elem in string:
    print (elem) ''' 

# РЕШЕНИЕ ЧЕРЕЗ СПИСКИ 
'''
string = 'a a a b c a a d c d d'.split() #только для строк. разбивает их на список символов от чего-то
print(string)
answer = ''
new_list = []
for elem in string:
    if elem in new_list:
        answer += elem + '_' + str(new_list.count(elem)) + ' '
    else:
        answer += elem + ' '
    new_list.append(elem)
print (answer)'''

# РЕШЕНИЕ ЧЕРЕЗ СЛОВАРЬ
string = 'a a a b c a a d c d d'.split() 
answer = ''
my_dict = {}
for elem in string:
    if elem in my_dict:
        answer += elem + '_' + str(my_dict[elem]) + ' '
        my_dict[elem] += 1
    else:
        answer += elem + ' '
        my_dict[elem] = 1
print (answer)

