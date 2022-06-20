import csv
import json

path_to_import_json_file = 'import_phonebook.json'
path_to_import_csv_file = 'import_phonebook.csv'

test_imported_data = [{'contact_id': '' ,'surname': 'Иванов', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}, 
                    {'contact_id': '' ,'surname': 'Петров', 'name': 'Петр', 'phone': '222', 'comment': 'Коллега'},
                    {'contact_id': '' ,'surname': 'Сидоров', 'name': 'Сидор', 'phone': '333', 'comment': 'Должен 1000'},
                    {'contact_id': '' ,'surname': 'Ромашкина', 'name': 'Маша', 'phone': '444', 'comment': 'Вкусные пирожки'},
                    {'contact_id': '' ,'surname': 'Василькова', 'name': 'Оля', 'phone': '555', 'comment': 'Большие глаза'}]

def import_txt():
    #path_to_file = 'phonebook.txt'
    
    return test_imported_data


def import_csv():
    # import csv
    # path_to_file = 'phonebook.csv'
    # results = []
    # with open (path_to_file) as csvfile:                           
    #     # Создаем объект reader, указываем символ-разделитель ";"
    #     file_reader = csv.reader(csvfile, delimiter= ";")
    #     for row in file_reader:
    #         results.append(row) # Каждую строку из phoneной книги добавляем в список результатов
    return test_imported_data

def import_json(path_to_import_json_file):
    
    # path_to_file = 'phonebook.json'
    return test_imported_data

# Выбираем формат файла phoneной книги
def choice_format():
    print('Телефонную книгу в каком формате изволите импотировать? \n.txt - 1 .csv - 2 .json - 3:')
    choice = int((input()))
    match choice:
        case 1: return import_txt()
        case 2: return import_csv()
        case 3: return import_json()
        case _ :
            print('Неизвестный формат файла')
            exit()


if __name__ == "__main__":
    from pprint import pprint
    pprint(choice_format(), sort_dicts=False)
    

  

