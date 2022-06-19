import time
from import_from_file import choice_format

main_menu = \
    'Выберите пункт меню:\n\
    1. \033[4mСписок контактов\033[0m\n\
    2. \033[4mПоиск контакта\033[0m\n\
    3. \033[4mДобавить контакт вручную\033[0m\n\
    4. \033[4mИзменить контакт\033[0m\n\
    5. \033[4mИмпорт контактов\033[0m\n\
    6. \033[4mЭкспорт контактов\033[0m\n\
    7. \033[4mВыход из приложения\033[0m'


def start_page():  # Starting page, choose number
    print('╔' + 48 * "=" + '╗')
    print('            \033[3;36mТелефонный справочник v0.1\033[0m')
    print('╚' + 48 * "=" + '╝')
    print(main_menu)
    print(50 * "=")
    print()
    command = input('\033[1mВыберите действие: \033[0m')
    print(50 * "•")
    return command


def show_contacts(data):  # 1 in menu
    if data != []:
        print('\033[4mСписок контактов:\033[0m')
        for item in range(len(data)):
            a = data[item]['contact_id']
            b = data[item]['surname']
            c = data[item]['name']
            d = data[item]['phone']
            e = data[item]['comment']
            print(f'{a}) {b}. {c}. {d}. {e}.')
        print(50 * "•")
    else:
        print('\033[33mСправочник пуст\033[0m')


def search_contact():
    search_request = input('Введите данные для поиска: ')
    print(50 * "=")
    return search_request


def add_contact():
    print('\033[3mДобавление контакта\033[0m')
    print(50 * "-")
    contact_surname = input('Введите фамилию ')  # plain text
    contact_name = input('Введите имя ')  # DD-MM-YY
    contact_number = input('Введите номер телефона')
    commentary = input('Комментарий')
    contact = [{'contact_id': '', 'surname': contact_surname, 'name': contact_name, 'phone': contact_number, 'comment': commentary}, ]
    return contact  # возвращение списка словаря


def change_contact():
    print('\033[4mИзменить контакт:\033[0m')
    print(50 * "~")
    contact_id = input('Выберите контакт для внесения изменений:')
    return int(contact_id)


def change_contact_content(one_contact):
    command = input('Что необходимо сделать: 1 - Изменить содержание \n 2 - Удалить контакт')#подменю для выбора  полей контакта
    if command == '1':
        contact_surname = input('Введите фамилию ')  # plain text
        contact_name = input('Введите имя ')  # DD-MM-YY
        contact_number = input('Введите номер телефона')
        commentary = input('Комментарий')
        one_contact = {'contact_id': '', 'surname': contact_surname, 'name': contact_name, 'phone': contact_number,
                        'comment': commentary}
    elif command == '2':
        one_contact['comment'] = 'Я что-то нажал и всё сломалось'  # удаление по ID
    return one_contact


def bye_mess():  # 6 in menu
    print('Работа завершена!')


def error_input():
    print('\033[5;31mОшибка!\033[0m')
    print('\033[21mПожалуйста введите число, соответствующее пункту меню.\033[0m')
    time.sleep(2)
    start_page()


def done_message():
    print('Выполнено!')


def import_contacts(import_list):
    print('\033[4mИмпорт контактов:\033[0m')
    choice_format()
    return

def export_contacts():
    return
