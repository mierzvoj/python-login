import sys
import os
import csv
import getpass


def run():
    if __name__ == '__main__': run()





def begin():
    global option
    print("Witaj")
    while True:
        try:
            option = int(input("Zaloguj albo zarejestruj się: 1 lub 2 "))
            if option in ['1', '2']:
                break
            if option == 1:
                login()
            else:
                register()
        except:
            print("Zacznij od nowa")
            break


def register():
    global islogged
    global name
    pattern = r'^[A-Z]{3}'
    print("Podaj login i hasło, aby się zarejestrować ")
    name = input("Podaj login w register, login musi zaczynać się trzema wielkimi literami i mieć jedną cyfrę: ")
    verifyLogin(name)
    while True:
        password = getpass.getpass("Podaj hasło o długości co najmniej 6 znaków z jedną cyfrą: ")
        if len(password) >= 6 and any(char.isdigit() for char in password):
            print("Poprawne hasło")
            break
        else:
            print("hasło musi mieć co najmniej 6 znaków i jedną cyfrę")
    with open('users.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([name, password])
        csvfile.close()
        print("Zarejestrowałeś się")
        islogged = True
    options()


def login():
    global islogged
    islogged = False
    while not islogged:
        userdata = []
        with open('users.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                userdata.append(row)
        name = input('Podaj swój login: ')
        password = getpass.getpass('Podaj swoje hasło ')
        col0 = [x[0] for x in userdata]
        col1 = [x[1] for x in userdata]
        if name in col0:
            for k in range(0, len(col0)):
                if col0[k] == name and col1[k] == password:
                    print("Zalogowałeś się ")
                    islogged = True
        else:
            print('Nieprawidłowy login lub hasło')
            print('Spróbuj się zarejestrować')
            register()
    options()


def verifyLogin(name):
    csv_file = csv.reader(open("users.csv", "r"))
    if not any(char.isdigit() for char in name):
        print('Podaj choć jedną cyfrę w loginie użytkownika')
        register()
    else:
        while True:
            for row in csv_file:
                if name == row[0]:
                    print("Użytkownik o takim loginie już istnieje")
                    print("Zarejestruj się jako nowy użytkownik o innym loginie")
                    register()
            break


def deleteEntry():
    member_name = input("Podaj login do usunięcia: ")
    with open('users.csv', 'r+', newline='') as in_file:
        rows = [row for row in csv.reader(in_file) if member_name not in row]
        in_file.seek(0)
        writer = csv.writer(in_file)
        writer.writerows(rows)


def options():
    while islogged:
        print("Witamy w programie logowania\n")
        print("Wybierz opcję menu lista: 1/szukaj: 2/usun: 3/zakoncz: 4\n")
        menu = int(input("podaj wybór: "))
        if menu == 1:
            displayUsers()
        elif menu == 2:
            searchByLogin()
        elif menu == 3:
            deleteEntry()
            print("Wybrany użytkownik został usunięty z rejestru, tej operacji nie można odwrócić")
        else:
            exit()


def displayUsers():
    data = []
    with open("users.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    print(data)


def searchByLogin():
    login = str(input("Podaj login do wyszukania: \n"))
    csv_file = csv.reader(open("users.csv", "r"))
    for row in csv_file:
        if login == row[0]:
            print(row)
            break
        else:
            print("---------nie znaleziono----------")


begin()
