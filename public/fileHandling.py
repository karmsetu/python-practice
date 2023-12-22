import os
import shutil as sh #to copy content of file
path = "d:\\python-practice\\public\src\\text.txt"
dest = "d:\\python-practice\\public\src\\copy.txt"
des2 = "d:\\python-practice\\public\src\\copy.txt"

def checkFile():
    if os.path.exists(path):
        print("exists")
        if os.path.isfile(path=path):
            print("that is a file")
    else:
        print("file does not exist")


def openFile(path, mode='r'):
    try:
        with open(path, mode) as file:
            print(file.read())
    except FileNotFoundError:
        print("that file was not found")

def writeFile(path, text):
    with open(str(path),'w') as file:
        file.write(text)

def copyFile(path, dest):
    sh.copyfile(path,dest)

def moveFile(src, des):
    try:
        if os.path.exists(des):
            print("there is already a file there")
        else:
            os.replace(src, des)
            print(src+"was moved")
    except FileNotFoundError:
        print(src+"not found")

def delFile(src):
    try:
        os.remove(src)
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("changes in file are not permissable")
    else:
        print(src+ "file eas deleted")