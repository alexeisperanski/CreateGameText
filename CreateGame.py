import os
global allFileName
global fileformat
fileformat = ".txt"
allFileName = ['start.txt']

def createf(fileName):  #создание файла
    fileS = os.listdir(path=".")
    for s in fileS:
        if fileName == s:
            print("Файл с данным именем уже существует")
            return False
    with open(fileName, "w"):
        print(f"Файл {fileName} создан")
    return True

def enterMission(fileName): #введение информация о ступени для чтения
    with open(fileName, "a") as file:
        file.write(input("Введите основной текст миссии: ") + "\n")
        otv = int(input("Введите сколько будет вариантов ответов: "))
        file.write(f"{otv}\n")
        for value in range(otv):
            file.write(input(f"Вариант ответа №{value + 1}: ") + "\n")
            file.write(input(f"Вариант реакции №{value + 1}: ") + "\n")
            link = input(f"Имя нового файла для перехода с ответ №{value + 1}: ") + fileformat
            file.write(f"{link}\n")
            if link in allFileName:
                print("Ссылка на уже готовый файл")
            else:
                allFileName.append(link)

print("Вы создёте первый шаг для игры\n")
Newfileform = input("Введите формат ваших файлов для записи(пустой, если .txt): ")
if Newfileform != "":
    fileformat = Newfileform

Tr = True
while Tr:
    if allFileName == []:
        Tr = False
        print("Все файлы уже созданы, программа имеет конец")
        continue
    print(f"\n\nЕщё не заполненные файлы: \n{allFileName[:]}")
    number = input("\nВыберите файл, который будете заполнять по номеру позиции\nИли нажмите Enter чтобы закончить: ")
    if number == "":
        print(f"Вы закончили запонение, но ваша игра имеет ссылки на несозданные файлы: {allFileName[:]}")
        Tr = False
        continue
    missionName = allFileName.pop(int(number) - 1)
    if createf(missionName):
        enterMission(missionName)









