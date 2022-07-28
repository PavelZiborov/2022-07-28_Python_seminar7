import calculator
import incoming
import logger
import menu
import sys
import view

def button_click():
    choice = menu.DrawMainMenu()
    if choice == '1':
        try:
            userInput = input('Введите выражение которое хотите посчитать: ')
            result = calculator.Calculator(incoming.StringToList(userInput))
            logger.Save(userInput, result)
            view.view_data(userInput, result)
            button_click()
        except:
            print('\nНЕИЗВЕСТНАЯ ОШИБКА!\n')
            logger.Save(userInput, 'НЕИЗВЕСТНАЯ ОШИБКА!')
    elif choice == '2':
        sys.exit
    else:
        print('\nОШИБКА ВЫБОРА МЕНЮ. ПОВТОРИТЕ!\n')
        button_click()