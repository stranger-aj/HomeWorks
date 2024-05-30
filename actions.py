import os


def create_contact():
    """Создание отформатированной строки данных для контакта"""
    surname = input("Введите фамилию: ").lower()
    name = input("Введите имя: ").lower()
    patronumic = input("Введите отчество: ").lower()
    phone = input("Введите телефон: ")
    address = input("Введите адрес: ").lower()
    return [surname, name, patronumic, phone, address]


def add_contact():
    """Добавление нового контакта в файл"""
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding="UTF-8") as file_a:
        for i in contact:
            if i != '':
                file_a.write(i + ' ')
            else:
                file_a.write('-empty-' + ' ')
        file_a.write('\n\n')


def search_contact():
    """Поиск и вывод контакта по ключевому слову, возвращает порядковые номера найденных контактов """
    num_contacts = []
    print("Варианты поиска контакта:\n"
          "1 - по Фамилии\n"
          "2 - по имени\n"
          "3 - по отчеству\n"
          "4 - по телефону\n"
          "5 - по адресу\n"
          )
    var = input("Введите вариант поиска: ")
    while var not in ('1', '2', '3', '4', '5'):
        print()
        print("Введены некорректные данные. Введите число от 1 до 5")
        var = input("Введите вариант поиска: ")
    index_var = int(var) - 1
    search = input("Введите данные для поиска: ").lower()

    with open('phonebook.txt', 'r', encoding="UTF-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")

    for i, contact_str in enumerate(list_contacts, 1):
        contact_lst = contact_str.split()
        if search in contact_lst[index_var]:
            num_contacts += [i]
            print(i, contact_str.title())
    if num_contacts == []:
        print("Контакты не найдены")
    return num_contacts


def print_contacts():
    """Печать справочника с указанием порядковых номеров контактов"""
    with open('phonebook.txt', 'r', encoding="UTF-8") as phonebook:
        list_contacts = phonebook.read().rstrip().split("\n\n")
        for i, contact in enumerate(list_contacts, 1):
            print(i, contact.title())

# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.


def copy_contact():
    name_of_file = input(
        "введите имя файла в который следует произвести копирование ( по умолчанию new_file.txt ): ")
    print_contacts()
    phonebook = open('phonebook.txt', 'r', encoding="UTF-8")
    new_file = open(name_of_file if name_of_file !=
                    "" else "new_file.txt", 'a', encoding="UTF-8")
    with phonebook, new_file:
        list_contacts = phonebook.read().rstrip().split("\n\n")
        number_of_contact = int(
            input("Введите номер контакта для копирования: "))
        while number_of_contact not in range(1, len(list_contacts)+1):
            number_of_contact = int(
                input("Некорректное значение. Введите номер контакта: "))
        with phonebook, new_file:
            new_file.write(list_contacts[number_of_contact-1] + '\n\n')


# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
def change_contact():
    found_contacts = search_contact()
    if found_contacts != []:
        phonebook = open('phonebook.txt', 'r', encoding="UTF-8")
        list_contacts = phonebook.read().rstrip().split("\n\n")
        number_of_contact = int(
            input("Введите номер контакта для изменения: "))
        while (number_of_contact not in found_contacts):
            number_of_contact = int(
                input("Некорректное значение. Введите номер контакта: "))
        phonebook.close()
        os.remove('phonebook.txt')
        file_a = open('phonebook.txt', 'a', encoding="UTF-8")
        for contact in list_contacts:
            if contact == list_contacts[number_of_contact - 1]:
                print("Хотите ли вы удалить этот контакт ?\n")
                print("1 - удалить")
                print("enter - изменить")
                if input() != '1':
                    file_a.close()
                    add_contact()
                    file_a = open('phonebook.txt', 'a', encoding="UTF-8")
            else:
                file_a.write(contact + '\n\n')
        file_a.close()

