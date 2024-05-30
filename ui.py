from actions import *

def interface():
    """"Пользовательский интерфейс"""
    with open('phonebook.txt', 'a', encoding="UTF-8"):
        pass
    command = ''
    while command != '5':
        print("\nВарианты действий:\n"
              "1 - ввод контакта\n"
              "2 - поиск контакта\n"
              "3 - копирование контакта\n"
              "4 - изменить контакт\n"
              "5 - выход\n"
              )
        command = input("Введите вариант действия: ")
        while command not in ('1', '2', '3', '4', '5'):
            print()
            print("Введены не корректные данные. Введите число от 1 до 5")
            command = input("Введите вариант действия: ")
        match command:
            case '1':
                add_contact()
            case '2':
                search_contact()
            case '3':
                copy_contact()
            case '4':
                change_contact()
            case '5':
                print("Сеанс завершен")