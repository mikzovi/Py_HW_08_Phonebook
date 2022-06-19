import csv

test_imported_data = [{'contact_id': '' ,'surname': 'Иванов', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}, 
                    {'contact_id': '' ,'contact_id': '', 'surname': 'Петров', 'name': 'Петр', 'phone': '222', 'comment': 'Коллега'},
                    {'contact_id': '' ,'surname': 'Сидоров', 'name': 'Сидор', 'phone': '333', 'comment': 'Должен 1000'},
                    {'contact_id': '' ,'surname': 'Ромашкина', 'name': 'Маша', 'phone': '444', 'comment': 'Вкусные пирожки'},
                    {'contact_id': '' ,'surname': 'Василькова', 'name': 'Оля', 'phone': '555', 'comment': 'Большие глаза'}]


def import_csv_to_json(file_csv): # нужно передать имя файла из которрого надо взять данные

    data_json = [] #сюда загоним список словарей который получип при преобразовании
    temp = [] 
     
    with open(file_csv,"r", newline="" ,encoding='UTF-8') as file: 
        reader_temp = csv.reader(file) 
        for row in reader_temp:
            temp.append(row)
        
    colone = list(temp.pop(0)) # мне нужен список ключей словаря. не нашла функцию для этого ['contact_id','surname', 'name', 'phone', 'comment'] 
    
    for element in temp:
        data_json.append(dict(zip(colone, element))) # собираем в список словарей
    
    return data_json    # получили данные в формате списка словарей. осталось записать его в файл




