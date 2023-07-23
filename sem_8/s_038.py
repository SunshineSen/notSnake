'''Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.'''

def show_data(fileName):
    print(' ФИО - телефон')
    with open(fileName, 'r', encoding='utf-8') as data:
        print(data.read())
    print('')


def export_data(fileName):
    with open(fileName, 'a', encoding = 'utf-8') as data: 
        fio = input('Введите ФИО: ')
        phone_number = input('Введите номер телефона: ')
        data.write(f'{fio} - {phone_number}\n')
        print(f'Добавлена запись : {fio} - {phone_number}\n')


def edit_data(fileName):
    print(' ФИО - телефон')
    with open(fileName, 'r', encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print('')
    index_delete_data = int(input('Введите номер строки для редактирования: ')) - 1
    tel_book_lines = tel_book.split('\n')
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(' - ')
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f'{fio} - {phone}'
    tel_book_lines[index_delete_data] = edited_line
    print(f'Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n')
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tel_book_lines))


def delete_data(fileName):
    print(' ФИО - телефон')
    with open(fileName, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
    print('')
    index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
    tel_book_lines = tel_book.split('\n')
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f'Удалена запись: {del_tel_book_lines}\n')
    with open(fileName, 'w', encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def main():
    user_selection = -1
    telephone = 'telephone.txt'

    while user_selection != 0:
        print('Выберите действие:')
        print('1 - Вывести информацию на экран')
        print('2 - Добавить новыую запись')
        print('3 - Изменить существующие данные')
        print('4 - Удалить данные')
        print('0 - Выход из программы')
        select = int(input('Выбор: '))
        if select == 1:
            show_data(telephone)
        elif select == 2:
            export_data(telephone)
        elif select == 3:
            edit_data(telephone)
        elif select == 4:
            delete_data(telephone)
        else:
            user_selection = 0


if __name__ == '__main__':
    main()