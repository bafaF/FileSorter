import os
import shutil
import sys

fileList = []
extensionList = []


def sortFile(filePath):
    for file in os.listdir(filePath):
        if os.path.isfile(os.path.join(filePath, file)):
            fileList.append(file)
            if os.path.splitext(file) not in extensionList:
                if os.path.splitext(file)[1] == "":
                    extensionList.append(os.path.splitext(file)[0])
                else:
                    extensionList.append(os.path.splitext(file)[1])


def creatingDir(path):
    for extension in extensionList:
        new_folder_name = str(extension).replace(".", "").lower() + "_folder"
        if not os.path.isdir(os.path.join(path, new_folder_name)):
            os.mkdir(os.path.join(path, new_folder_name))
    for file in fileList:
        for directory in os.listdir(path):
            current_path = path + "\\" + directory
            if os.path.isdir(os.path.join(current_path)) and str(os.path.splitext(file)[1]).replace(".",
                                                                                                    "").lower() in directory:
                if file not in os.listdir(os.path.join(path, directory)):
                    shutil.move(os.path.join(path, file), os.path.join(current_path))
                else:
                    print("File already")
                break


def start(path):
    sortFile(path)
    creatingDir(path)


start(sys.argv[1])
