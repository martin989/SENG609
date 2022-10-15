from Assignment10.Form import Form
from Assignment10.Data import Data
from tkinter import *


def main():
    file_name = "C:\\Users\\Martin\\Desktop\\Masters\\Fall 2022 SENG-609\\Week 10\\Dataset.csv"
    data = Data(file_name)
    root = Tk()
    form = Form(root, data)
    root.mainloop()


if __name__ == '__main__':
    main()
