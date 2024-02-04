def work_with_phonebook():
	



    phone_book=read_txt('phonebook.txt')

    while True:
        choice=show_menu()
        if choice == 6:
            break
        elif choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию: ')
            find_by_lastname(phone_book,last_name)
        elif choice==3:
            number=input('Введите номер телефона: ')
            print(find_by_number(phone_book,number))
        elif choice==4:
            user_data=input('Введите новые данные(Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        elif choice==5:
            filename = input('Введите имя для сохраняемого файла: ')
            write_txt(filename , phone_book)
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)


        choice=show_menu()


def show_menu():
    print("Выберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice



# Иванов,       Иван ,   111,  описание Иванова
# Петров,      Петр ,    222,  описание Петрова
# Васичкина , Василиса , 333 , описание Васичкиной
# Питонов,    Антон,     777,    умеет в Питон

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    for i in phone_book:
        print(i)

def find_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            print(i)

def find_by_number(phone_book,number):
    for i in phone_book:
        if i['Телефон'] == number:
            print(i)

def add_user(phone_book,user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_res = dict(zip(fields, user_data.split(',')))
    phone_book.append(new_res)



work_with_phonebook()