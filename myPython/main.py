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
    pattern = re.compile(r'')
    print("Podaj login i hasło, aby się zarejestrować ")
    name = input("Podaj login: ")
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
    name = input("Podaj login: ")
    password = getpass.getpass("Podaj hasło: ")
    with open('users.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == name and row[1] == password:
                csvfile.close()
                print("Zalogowałeś się")
                islogged = True
                options()
                break
            else:
                print("Błędny login lub hasło")
                begin()


def verifyLogin():
    csv_file = csv.reader(open("users.csv", "r"))
    while True:
        name = input("Podaj login: ")
        for row in csv_file:
            if name == row[0]:
                error = print("Użytkownik o takim loginie już istnieje")
            # register()
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
            print("blob")
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
        else:
            print("--------------------------")
            break


begin()
