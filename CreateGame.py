import string
import math
import fileinput
import os
global allFileName
global fileformat
fileformat = ".txt"
allFileName = []
allFileName = ['start.txt']

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
            file.write(input(f"Вариант ответа №{value + 1}: ") + "\n")
            file.write(input(f"Вариант реакции №{value + 1}: ") + "\n")
            link = input(f"Имя нового файла для перехода с ответ №{value + 1}: ")
            file.write(f"{link}\n")
            if link in allFileName:
                print("Ссылка на уже готовый файл")
            else:
                allFileName.append(link)

print("Вы создёте первый шаг для игры\n")
Newfileform = input("Введите формат ваших файлов для записи(пустой, если .txt): ")
if Newfileform != "":
    fileformat = Newfileform
missionName = input("Введите имя нового файла")
if createf(missionName):
    enterMission(missionName)
Tr = True
while Tr:
    number = input(allFileName, "\nВыберите файл, который будете создавать по номеру позиции\nИли нажмите Enter чтобы закончить: ")
    if number == "":
        Tr = False
        continue
    missionName = allFileName.pop(number - 1)
    if createf(missionName):
        enterMission(missionName)










