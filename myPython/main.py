import sys
import os
import csv
from csv import writer
import userlogin
import userregister
import re
import getpass





def run():
    if __name__ == '__main__': run()


def begin():
    global option
    print("Witaj")
    while True:
        option = int(input("Zaloguj albo zarejestruj się: 1 lub 2 "))
        if option in ['1', '2']:
            break
        if option == 1:
            login()
        else:
            register()


def register():
    global islogged
    global name
    pattern = re.compile(r'')
    print("Podaj login i hasło, aby się zarejestrować ")
    name = input("Podaj login 1: ")
    verifyLogin()
    while True:
        password = getpass.getpass("Podaj hasło: ")
        if (len(password) < 6):
            while True:
              print("hasło musi mieć co najmniej 6 znaków")
              password = getpass.getpass("Podaj hasło: ")
              if(len(password) >= 6):
                break
              else:
                print("hasło musi mieć co najmniej 6 znaków")
        else:
            print("Poprawne hasło")
        break
    with open('users.csv', 'a', newline='') as csvfile:
      csv_writer = csv.writer(csvfile)
      csv_writer.writerow([name, password])
      csvfile.close()
      print("Zarejestrowałeś się")
      islogged = True
    options()


def login():
    print("tu login")
    global islogged
    islogged = False
    with open('users.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        while True:
            name = input("Podaj swój login: ").title()
            for row in csv_reader:
              if row[0] != name:
                print("Nie jesteś zarejestrowany")
                print()
            else:
                break
            break
        while True:
            password = getpass.getpass("Podaj hasło: ")
            for row in csv_reader:
                if row[0] != password:
                    print("Hasło niepoprawne")
                    print()
            else:
                break
            break

        print()
        print("Zalogowany")
        islogged = True
        options()

def verifyLogin():
    csv_file = csv.reader(open("users.csv", "r"))
    while True:
        for row in csv_file:
            if name == row[0]:
                print("Użytkownik o takim loginie już istnieje")
            break
            print("Zarejestruj się jako nowy użytkownik")
            register()
        else:
            print("Login ok")
            break


def deleteEntry():
    member_name = input("Podaj login do usunięcia: ")

    with open('users.csv', 'r+') as in_file:
        reader = csv.reader(in_file)
        rows = [row for row in csv.reader(in_file) if member_name not in row]
        in_file.seek(0)
        in_file.truncate()
        writer = csv.writer(in_file)
        writer.writerows(rows)


def options():
    print(islogged)
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
            print("Wybrany użytkownik został usunięty z rejestru")
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
