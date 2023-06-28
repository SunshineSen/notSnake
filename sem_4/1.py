import time # from time import time
from sys import getsizeof
#  time профилирование по времени (сколько выполняется программа)
#  sys профилирование по памяти (сколько занимает)
start = time.time()  # start = time ()
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
print (my_dict)
finish = time.time()
print (finish - start)
print (getsizeof(my_dict))
print (getsizeof(answer))