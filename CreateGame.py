import string
import math
import fileinput
import os

def createf(fileName):
    fileS = os.listdir(path=".")
    print(fileS)
    for s in fileS:
        if fileName == s:
            return False
    with open(fileName, "w"):
        print("Файл создан")
    return True

createf("first")
createf("second")
createf("first")



