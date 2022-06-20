import csv
# считывает данные из файла в формате csv и создает список словарей для дальнейшей работы с ним.

def import_csv_to_json(file_csv): # нужно передать имя файла из которрого надо взять данные

    data_json = [] #сюда загоним список словарей который получип при преобразовании
    temp = [] 
     
    with open(file_csv,"r", newline="" ,encoding='UTF-8') as file: 
        reader_temp = csv.reader(file) 
        for row in reader_temp:
            temp.append(row)
        
    colone = list(temp.pop(0)) # список ключей словаря. 
    
    for element in temp:
        data_json.append(dict(zip(colone, element))) # собираем в список словарей
    
    print(data_json)

    return data_json    # получили данные в формате списка словарей. осталось добавить эти строки в базу

