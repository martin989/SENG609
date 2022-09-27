from Assignment5.Form import Form
from Assignment5.Data import Data
from tkinter import *


def main():
    file_name = "C:\\Users\\Martin\\Desktop\\Masters\\Fall 2022 SENG-609\\Week 4\\dataset.csv"
    data = Data(file_name)
    root = Tk()
    form = Form(root, data)
    root.mainloop()


if __name__ == '__main__':
    main()
