''' Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea 
shells on the sea shore I'm sure that the shells are sea shore shells '''

st = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
words = st.split()
print (len(set(words)))
my_dict = {}
for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1
values = my_dict.values()
max_value = max(values)
print (max_value)
print (my_dict)
for key, value in my_dict.items():
    if value == max_value:
        print (key)