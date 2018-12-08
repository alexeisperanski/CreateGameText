fileInform = []

def readFile(fileGame):
    with open(fileGame, "r") as file:
        fileString = file.read().split("\n")
    allOtvet = []
    print(fileString[0])
    for i in range(int(fileString[1])):  #Перенос ответов в новый массив
        otvet = []
        for j in range(3):
            otvet.append(fileString[2 + 3 * i + j])
        allOtvet.append(otvet)
    return allOtvet

newOpen = "start.txt"
while newOpen != "exit.txt":
    fileInform = readFile(newOpen)
    value = len(fileInform)
    for i in range(value):
       print(f"{i + 1}. {fileInform[i][0]}")
    numb = int(input(f"Выберете вариант действия от 1 до {value}"))
    print(fileInform[numb - 1][1])
    newOpen = fileInform[numb - 1][1]
