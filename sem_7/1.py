'''
def summ(x, a):
    return x + a

def calc(op, x, y):
    return op(x, y)

print (calc (summ, 5, 8)) # print(calc(lambda x, y: x + y, 5, 8))
# calc - функция высшего порядка так как она вызывает другую функцию
'''
'''
def kvadrat(x):
    return x**2
# чтобы укоротить код создаем лямбда функцию
a = lambda x: x**2
print (a(4)) '''

'''
my_list = list(map(int, input().split()))
print(my_list)
# map принимает функцию и обьект к которому ее применить. тут она функцией int бежит по списку и делает его из строк числами
'''
'''
a = [1, 5, 4, 3, 8]
answer = list( map (lambda x: x**2, a))
print (answer) '''

'''
#  filter принимает функцию и список.
a = [1, 16, 4, 5, 8, 3, 8]
b = list(filter( lambda x: x%2 == 0, a))
print(b) '''

#нумерует список enumerate
name = ['Tom', 'Loi', 'Kate']

for id, name in enumerate(name):
    print(id, name)