from tkinter import *
from tkinter import ttk


class House():
    def __init__(self, sqft, num_bed, num_bath, sale_price):
        self.sqft = sqft
        self.num_bed = num_bed
        self.num_bath = num_bath
        self.sale_price = sale_price


class Form():
    def __init__(self, root, list):
        self.list = list

        root.title("House Reader")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.bedrooms = IntVar()
        bedrooms_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.bedrooms)
        bedrooms_entry.grid(column=2, row=1, sticky=(W, E))

        self.bathrooms = IntVar()
        bathrooms_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.bathrooms)
        bathrooms_entry.grid(column=2, row=2, sticky=(W, E))

        self.size = IntVar()
        size_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.size)
        size_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.mainframe, text="Bedrooms").grid(column=3, row=1, sticky=W)
        ttk.Label(self.mainframe, text="Bathrooms").grid(column=3, row=2, sticky=W)
        ttk.Label(self.mainframe, text="Size").grid(column=3, row=3, sticky=W)

        self.choice_bedrooms = IntVar()
        self.choice_bedrooms.set(1)
        ttk.Radiobutton(self.mainframe, text="=", variable=self.choice_bedrooms, value=1).grid(column=4, row=1,
                                                                                               sticky=W)
        ttk.Radiobutton(self.mainframe, text="<=", variable=self.choice_bedrooms, value=2).grid(column=5, row=1,
                                                                                                sticky=W)
        ttk.Radiobutton(self.mainframe, text=">=", variable=self.choice_bedrooms, value=3).grid(column=6, row=1,
                                                                                                sticky=W)

        self.choice_bathrooms = IntVar()
        self.choice_bathrooms.set(1)
        ttk.Radiobutton(self.mainframe, text="=", variable=self.choice_bathrooms, value=1).grid(column=4, row=2,
                                                                                                sticky=W)
        ttk.Radiobutton(self.mainframe, text="<=", variable=self.choice_bathrooms, value=2).grid(column=5, row=2,
                                                                                                 sticky=W)
        ttk.Radiobutton(self.mainframe, text=">=", variable=self.choice_bathrooms, value=3).grid(column=6, row=2,
                                                                                                 sticky=W)

        self.choice_size = IntVar()
        self.choice_size.set(1)
        ttk.Radiobutton(self.mainframe, text="=", variable=self.choice_size, value=1).grid(column=4, row=3,
                                                                                           sticky=W)
        ttk.Radiobutton(self.mainframe, text="<=", variable=self.choice_size, value=2).grid(column=5, row=3,
                                                                                            sticky=W)
        ttk.Radiobutton(self.mainframe, text=">=", variable=self.choice_size, value=3).grid(column=6, row=3,
                                                                                            sticky=W)

        ttk.Button(self.mainframe, text="Calculate", command=self.find).grid(column=3, row=5, sticky=W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.string = StringVar()
        self.stringbedrooms = StringVar()
        self.stringbathrooms = StringVar()
        self.stringsqft = StringVar()
        ttk.Label(self.mainframe, textvariable=self.string).grid(column=1, row=10, columnspan=10, sticky=(W, E))
        ttk.Label(self.mainframe, textvariable=self.stringbedrooms).grid(column=1, row=11, columnspan=10, sticky=(W, E))
        ttk.Label(self.mainframe, textvariable=self.stringbathrooms).grid(column=1, row=12, columnspan=10,
                                                                          sticky=(W, E))
        ttk.Label(self.mainframe, textvariable=self.stringsqft).grid(column=1, row=14, columnspan=10, sticky=(W, E))

        root.bind("<Return>", self.find)

    def conditionCheck(self, var1, var2, var3):
        if ((var1 == 0)
                or ((var2 == var1) & (var3 == 1))
                or ((var2 <= var1) & (var3 == 2))
                or ((var2 >= var1) & (var3 == 3))):
            return True
        else:
            return False

    def getAverageCost(self, list):
        cost = 0
        if (len(list) == 0):
            return cost
        else:
            for h in list:
                cost = cost + int(h.sale_price)
            return cost / len(list)

    def getConditional(self, var):
        if (var == 1):
            return "="
        elif (var == 2):
            return "<="
        else:
            return ">="

    def find(self, *args):
        new_list = []
        bedrooms = self.bedrooms.get()
        bathrooms = self.bathrooms.get()
        size = self.size.get()
        pick_bedrooms = self.choice_bedrooms.get()
        pick_bathrooms = self.choice_bathrooms.get()
        pick_size = self.choice_size.get()
        try:
            for h in self.list:
                check = False
                check1 = self.conditionCheck(bedrooms, int(h.num_bed), pick_bedrooms)
                check2 = self.conditionCheck(bathrooms, int(h.num_bath), pick_bathrooms)
                check3 = self.conditionCheck(size, int(h.sqft), pick_size)
                if (bedrooms > 0) or (bathrooms > 0) or (size > 0):
                    check = True
                if check & check1 & check2 & check3:
                    new_list.append(h)

            self.string.set("")
            self.stringbedrooms.set("")
            self.stringbathrooms.set("")
            self.stringsqft.set("")
            if len(new_list) > 0:
                self.string.set("The average cost for " + str(len(new_list)) + " houses equals $" + str(
                    round(self.getAverageCost(new_list), 2)))
                if bedrooms > 0:
                    self.stringbedrooms.set(
                        "with " + self.getConditional(
                            pick_bedrooms) + " " + str(bedrooms) + " bedrooms")
                else:
                    self.stringbedrooms.set("with >= 0 bedrooms")

                if bathrooms > 0:
                    self.stringbathrooms.set(
                        "with " + self.getConditional(
                            pick_bathrooms) + " " + str(
                            bathrooms) + " bathrooms")
                else:
                    self.stringbathrooms.set("with >= 0 bathrooms")

                if size > 0:
                    self.stringsqft.set(
                        "with " + self.getConditional(
                            pick_size) + " " + str(size) + " sq ft")
                else:
                    self.stringsqft.set("with >= 0 sq ft")
            else:
                self.string.set("No Matches Found!")

        except ValueError:
            pass


class FileHandler():
    # Create Object from File
    def object_from_file(filename):
        list = []
        with open(filename, "r") as file:
            next(file)
            cells = []
            for line in file:
                line = line.split("\n")
                cells = line[0].split(",")
                list.append(House(cells[0], cells[1], cells[2], cells[3]))
        file.close()
        return list


def main():
    # Add File name here
    file_name = "house_data.csv"
    list = FileHandler.object_from_file(str(file_name))
    root = Tk()
    Form(root, list)
    root.mainloop()


if __name__ == '__main__':
    main()
