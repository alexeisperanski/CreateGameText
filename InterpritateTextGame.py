fileInform = []

def readFile(fileGame): #Чтение файла и отсортировка лишнего
    with open(fileGame, "r") as file:
        fileString = file.read().split("\n")
    allOtvet = []
    print(f"\n{fileString[0]}") #вывод текста
    for i in range(int(fileString[1])):  #Перенос ответов в новый массив по кол-ву ответов
        otvet = []
        for j in range(3):
            otvet.append(fileString[2 + 3 * i + j])
        allOtvet.append(otvet)
    return allOtvet #Возвращение массива

newOpen = "start.txt"   # Выбор первого файла
pastOpen = "exit.txt"   # Выбор последнего файла

while newOpen != pastOpen:
    fileInform = readFile(newOpen)  # Вывод текста и получения массива ответов
    value = len(fileInform)
    for i in range(value):  # Вывод вариантов ответов
        print(f"{i + 1}. {fileInform[i][0]}")
    numb = int(input(f"Выберете вариант действия от 1 до {value}: "))
    print(f"{fileInform[numb - 1][1]}") # Ответ на выбор и следующий файл для открытия
    newOpen = fileInform[numb - 1][2]

readFile(newOpen)
print("\nСпасибо за игру!")