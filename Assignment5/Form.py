from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntry


class Form():
    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.found = StringVar()
        self.root.title('Pay Estimate for Arizona')
        self.root.geometry("500x750+10+10")

        self.lbl0 = Label(self.root, text='Enter Information to calculate pay')
        self.lbl0.place(x=100, y=10)

        self.lbl2 = Label(self.root, text='Job Title')
        self.lbl2.place(x=100, y=100)
        t2complete = self.data.getUnique("Job Title")
        self.t2 = AutocompleteEntry(self.root, width=15, font=('Times', 12), completevalues=t2complete)

        self.t2.place(x=200, y=100)

        self.lbl3 = Label(self.root, text='Department')
        self.lbl3.place(x=100, y=150)
        t3complete = self.data.getUnique("Department")
        self.t3 = AutocompleteEntry(self.root, width=15, font=('Times', 12), completevalues=t3complete)
        self.t3.place(x=200, y=150)

        self.lbl4 = Label(self.root, text='Hire Date')
        self.lbl4.place(x=100, y=200)
        t4complete = self.data.getUnique("Hire Date")
        self.t4 = AutocompleteEntry(self.root, width=15, font=('Times', 12), completevalues=t4complete)
        self.t4.place(x=200, y=200)

        self.lbl5 = Label(self.root, text='Benefits Category')
        self.lbl5.place(x=100, y=250)
        self.t5 = Entry(bd=3, width=15, font=('Times', 12))
        self.t5.place(x=200, y=250)

        options = [
            "Full Time",
            "Part Time"
        ]
        self.clicked = StringVar()
        self.clicked.set("Full Time")
        self.opm6 = OptionMenu(self.root, self.clicked, *options)
        self.opm6.place(x=200, y=300)
        self.lbl6 = Label(self.root, text='Hours')
        self.lbl6.place(x=100, y=300)

        self.lbl7 = Label(self.root, text='Testing Set Size')
        self.lbl7.place(x=100, y=350)
        self.t7 = Entry(bd=3, width=15, font=('Times', 12))
        self.t7.place(x=200, y=350)

        # Results
        self.btn10 = Button(self.root, text='Result')
        self.b10 = Button(self.root, text='Result', command=self.result)
        self.b10.place(x=100, y=400)
        options2 = [
            "Linear Regression",
            "Linear Regression Train",
            "Decision Trees",
            "Decision Trees Train"
        ]
        self.clicked2 = StringVar()
        self.clicked2.set("Linear Regression")
        self.opm7 = OptionMenu(self.root, self.clicked2, *options2)
        self.opm7.place(x=200, y=400)
        self.lbl10 = Label(self.root, text='Result')
        self.lbl10.place(x=100, y=450)
        self.t10 = Entry(self.root, textvariable=self.found)
        self.t10.place(x=200, y=450)

        # Graph
        graphOptions = self.data.getNumericColumns()
        self.clicked3 = StringVar()
        self.clicked3.set(graphOptions[0])
        self.opm15 = OptionMenu(self.root, self.clicked3, *graphOptions)
        self.opm15.place(x=200, y=500)
        self.lbl15 = Label(self.root, text='Select Graph')
        self.lbl15.place(x=100, y=500)
        self.btn16 = Button(self.root, text='Graph')
        self.b16 = Button(self.root, text='Graph', command=self.graph)
        self.b16.place(x=100, y=550)

        # Data Linear Regression
        self.lbl20 = Label(self.root, text='Linear Regression')
        self.lbl20.place(x=50, y=600)
        self.lbl21 = Label(self.root, text='Training Set Error')
        self.lbl21.place(x=50, y=650)
        self.lbl22_txt = StringVar()
        self.lbl22 = Label(self.root, textvariable=self.lbl22_txt)
        self.lbl22.place(x=50, y=675)
        self.lbl23 = Label(self.root, text='Test Set Error')
        self.lbl23.place(x=50, y=700)
        self.lbl24_txt = StringVar()
        self.lbl24 = Label(self.root, textvariable=self.lbl24_txt)
        self.lbl24.place(x=50, y=725)

        # Data Decision Trees
        self.lbl30 = Label(self.root, text='Decision Trees')
        self.lbl30.place(x=300, y=600)
        self.lbl31 = Label(self.root, text='Training Set Error')
        self.lbl31.place(x=300, y=650)
        self.lbl32_txt = StringVar()
        self.lbl32 = Label(self.root, textvariable=self.lbl32_txt)
        self.lbl32.place(x=300, y=675)
        self.lbl33 = Label(self.root, text='Training Set Error')
        self.lbl33.place(x=300, y=700)
        self.lbl34_txt = StringVar()
        self.lbl34 = Label(self.root, textvariable=self.lbl34_txt)
        self.lbl34.place(x=300, y=724)

    def result(self):
        t2_text = self.t2.get()
        t3_text = self.t3.get()
        t4_text = self.t4.get()
        t5_text = self.t5.get()
        if (self.clicked.get() == "Full Time"):
            t6_text = "F"
        else:
            t6_text = "P"

        txt_clicked2 = self.clicked2.get()

        if (txt_clicked2 == "Linear Regression"):
            self.t10.insert(0, str(self.data.getLinearRegression(t2_text, t3_text, t4_text, t5_text, t6_text)))
        elif (txt_clicked2 == "Linear Regression Train"):
            results = self.data.getLinearRegressionTrain(self.t7.get())
            self.lbl22_txt.set(str(results[0]))
            self.lbl24_txt.set(str(results[1]))
        elif (txt_clicked2 == "Decision Trees"):
            self.t10.insert(0, str(self.data.getDecisionTree(t2_text, t3_text, t4_text, t5_text, t6_text)))
        else:
            results = self.data.getDecisionTreeTrain(self.t7.get())
            self.lbl32_txt.set(str(results[0]))
            self.lbl34_txt.set(str(results[1]))

    def graph(self):
        self.data.visualPreCleanGraph(self.clicked3.get())
