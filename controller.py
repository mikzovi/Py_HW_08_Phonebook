import interface
import database_module
import logger


def run():
    
    while True:
    
        command = interface.start_page()

        match command:
            case '1':     # Список всех дел
                data = database_module.get_all_deals() ## прошу дописать функцию в data_base
                interface.show_deals(data) ## предлагаю не вводить команду юзера, а после вывода дел вызывать главное меню + дописать исключение, если 'baseIsEmpty'

            case '2': # Список дел по статусу
                status = interface.show_deals_by_status()
                while status not in range(1,6):
                    interface.error_input()
                    status = interface.show_deals_by_status()
                data = database_module.get_status_deal(status) ## прошу переименовать функцию get_data_undone в data_base
                interface.show_deals(data)
            
            
            case '3': # Добавить дело

                new_deal = interface.add_deal() # user_data - введенные юзером данные в удобном формате. Здесь я их преобразую в стандартный наш словарь и передам в data_base и logger
                database_module.add_deal(new_deal)
                logger.add(new_deal, 'added')
                interface.done_message()

            case '4': # Изменить дело
                data = database_module.get_all_deals()
                interface.show_deals(data)
                deal_id = interface.change_deal()
                one_deal = database_module.get_one_deal(deal_id)
                changed_deal = interface.change_deal_content(one_deal)
                if changed_deal['status'] == 10:
                    database_module.delete_deal(changed_deal['deal_id'])
                    logger.add(changed_deal, 'deleted')
                else:
                    database_module.change_deal(changed_deal)
                    logger.add(changed_deal, 'changed')
            
            case '5': # Выход
                interface.bye_mess() # прошу дописать функцию bye в interface (прощание с юзером)
                break

            case '7': # экспорт
                interface.export_contacts() # 
                break
            
            case _:
                interface.error_input() # прошу дописать функцию error_input в interface, которая выведет сообщение что-то вроде "Введены некорректные данные"


def change_action(user_answer: dict):
    match user_answer['user_choise']:
        case 1: # завершить дело
            return
        
        case 2: # изменить дело
            return

        case 3: # удалить дело
            return
