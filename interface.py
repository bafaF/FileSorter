import os
import shutil
import tkinter as tk
from tkinter.filedialog import *


class FileSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('File sorter')
        self.selected_directory = None

        self.select_directory_button = tk.Button(root, text='Select directory', command=self.select_directory)
        self.select_directory_button.pack()

        self.selected_directory_label = tk.Label(root)
        self.selected_directory_label.pack()

        self.sort_directory_button = tk.Button(root, text='Sort directory', command=self.sort_directory)
        self.sort_directory_button.pack()

        self.fileList = []
        self.extensionList = []

        self.end_sorting_label = tk.Label(root)
        self.end_sorting_label.pack()

    def select_directory(self):
        self.selected_directory = askdirectory(title="Sélectionnez un dossier")
        self.selected_directory_label.config(text=self.selected_directory)
        self.end_sorting_label.config(text="")

    def sort_directory(self):
        self.fileList = []
        self.extensionList = []
        self.sort_files()
        self.creatingDir()
        self.end_sorting_label.config(text="Directory has been sorted")

    def sort_files(self):
        for file in os.listdir(self.selected_directory):
            if os.path.isfile(os.path.join(self.selected_directory, file)):
                self.fileList.append(file)
                if os.path.splitext(file) not in self.extensionList:
                    if os.path.splitext(file)[1] == "":
                        self.extensionList.append(os.path.splitext(file)[0])
                    else:
                        self.extensionList.append(os.path.splitext(file)[1])

    def creatingDir(self):
        for extension in self.extensionList:
            new_folder_name = str(extension).replace(".", "") + "_folder"
            if not os.path.isdir(os.path.join(self.selected_directory, new_folder_name)):
                os.mkdir(os.path.join(self.selected_directory, new_folder_name))
        for file in self.fileList:
            for directory in os.listdir(self.selected_directory):
                current_path = self.selected_directory + "/" + directory
                if os.path.isdir(os.path.join(current_path)) and str(os.path.splitext(file)[1]).replace(".",
                                                                                                        "").lower() in directory:
                    if file not in os.listdir(os.path.join(self.selected_directory, directory)):
                        shutil.move(os.path.join(self.selected_directory, file), os.path.join(current_path))
                    break


if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.geometry("250x150")
    app = FileSorterApp(fenetre)
    fenetre.mainloop()
