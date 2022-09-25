from tkinter import *
from tkinter import ttk


class Form():
    def __init__(self, root):
        root.title("Salary Predictor")

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

        ttk.Button(self.mainframe, text="Calculate", command=self.graph).grid(column=3, row=5, sticky=W)

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

        root.bind("<Return>", self.graph)
        root.mainloop()

    def graph(self, *args):
        print("nothing")
