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


granted = False


def grant():
    global granted
    granted = True
    return granted


def verifyLogin(name):
    pass


def deleteEntry():

    member_name = input("Podaj login do usunięcia: ")

    with open('users.csv', 'r+') as in_file:
        reader = csv.reader(in_file)
        rows = [row for row in csv.reader(in_file) if member_name not in row]
        in_file.seek(0)
        in_file.truncate()
        writer = csv.writer(in_file)
        writer.writerows(rows)


def begin():
    global option
    print("Witaj")
    option = input("Zaloguj albo zarejestruj się: log/rej ")
    if (option != "log" and option != "rej"):
        begin()


def access(option):
    if (option == "log"):
        name = input("Podaj login: ")
        password = getpass.getpass("Podaj hasło: ")
        login(name, password)

    else:
        print("Podaj login i hasło, aby się zarejestrować ")
        name = input("Podaj login: ")
        pattern = re.compile(r'')
        while True:
          password = getpass.getpass("Podaj hasło: ")
          if(len(password) < 6):
                print("hasło musi mieć co najmniej 6 znaków")
          else:
             print("Poprawne hasło")
             break
        register(name, password)


def options():
    print("Witamy w programie logowania\n")
    success = True
    while success:
        print("Wybierz opcję menu lista: 1/szukaj: 2/usun: 3/zakoncz: 4\n")
        menu = int(input("podaj wybór: "))
        if menu == 1:
            displayusers()
        elif menu == 2:
            searchByLogin()
        elif menu == 3:
            deleteEntry()
            print("blob")
        else:
            exit()


def displayusers():
    data = []
    with open("users.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    print(data)


def searchByLogin():
    login = input("Podaj login do wyszukania: \n")
    csv_file = csv.reader(open("users.csv", "r"))
    for row in csv_file:
        if login == row[0]:
            print(row)
        else:
            print("--------------------------")


def register(name, password):
    with open('users.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([name, password])
        csvfile.close()
    print("Zarejestrowałeś się")
    grant()


success = True


def login(name, password):
    global success
    success = False
    with open('users.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == name and row[1] == password:

                csvfile.close()
                print("Zalogowałeś się")
                grant()
                options()
                success = True

                break
            else:
                print("-------------")
                # break

        begin()
        access(option)
begin()
access(option)

while success:
        print(granted)
        print("JESTEM W WHILE")
        options()



