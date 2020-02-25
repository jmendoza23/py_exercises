import os

pathS = "C:/Users/jmend/Documents/White/pyrepaso/user_managment"


def listFiles(path):
    for sChild in os.listdir(pathS):
        sChildPath = os.path.join(pathS, sChild)
        if os.path.isdir(sChildPath):
            listFiles(sChildPath)
        else:
            print(sChildPath)


listFiles(pathS)