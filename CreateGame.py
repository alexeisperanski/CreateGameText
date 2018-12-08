import string
import math
import fileinput
import os
global allFileName
allFileName = []

def createf(fileName):
    fileS = os.listdir(path=".")
    print(fileS)
    for s in fileS:
        if fileName == s:
            print("Файл с данным именем уже существует")
            return False
    with open(fileName, "w"):
        print("Файл создан")
    return True

def enterMission(fileName):
    with open(fileName, "a") as file:
        file.write(input("Введите основной текст миссии: ") + "\n")
        otv = int(input("Введите сколько будет вариантов ответов: "))
        file.write(f"{otv}\n")
        for value in range(otv):
            file.write(input(f"Вариант ответа №{value}: ") + "\n")
            file.write(input(f"Вариант реакции №{value}: ") + "\n")
            link = input(f"Имя нового файла для перехода с ответ №{value}: ")
            file.write(f"{link}\n")
            if link in allFileName:
                print("Ссылка на уже готовый файл")
            else:
                allFileName.append(link)






