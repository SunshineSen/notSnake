# генератор обозначается в круглых скобках 
b = (i for i in range(10**100))
print(b)
i = next (b)
print (i)
i = next (b)
print (i)
# каждый раз используя next генератор переходит к следующему числу не храня их в памяти

# цикл for может перебирать и генератор
b = (i for i in range(10**100) if i%2 == 1)
for i in b:
    print(i)
    if i > 100:
        break