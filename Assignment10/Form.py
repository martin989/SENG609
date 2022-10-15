from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntry


class Form():
    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.root.title('Pay Estimate for Arizona')
        self.root.geometry("900x500+10+10")
        self.test()
        self.train()

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
            self.t10.insert(0, str(self.data.getPredict(t2_text, t3_text, t4_text, t5_text, t6_text, 'lin_model.pkl')))
        elif (txt_clicked2 == "Decision Trees"):
            self.t10.insert(0, str(self.data.getPredict(t2_text, t3_text, t4_text, t5_text, t6_text, 'dec_model.pkl')))
        elif (txt_clicked2 == "KNN"):
            self.t10.insert(0, str(self.data.getPredict(t2_text, t3_text, t4_text, t5_text, t6_text, 'knn_model.pkl')))
        elif (txt_clicked2 == "Neural Network"):
            self.t10.insert(0, str(self.data.getPredict(t2_text, t3_text, t4_text, t5_text, 'nn_model.pkl')))

    def trainresult(self):
        txt_clicked2 = self.clicked50.get()

        if (txt_clicked2 == "Linear Regression Train"):
            results = self.data.getLinearRegressionTrain(.3)
            self.lbl56_txt.set(str(results[0]))
            self.lbl58_txt.set(str(results[1]))
        elif (txt_clicked2 == "Decision Trees Train"):
            results = self.data.getDecisionTreeTrain(.3)
            self.lbl62_txt.set(str(results[0]))
            self.lbl64_txt.set(str(results[1]))
        elif (txt_clicked2 == "KNN Train"):
            results = self.data.getKNNTrain(.3, 2)
            self.lbl72_txt.set(str(results[0]))
            self.lbl74_txt.set(str(results[1]))
        elif (txt_clicked2 == "Neural Network Train"):
            results = self.data.getNNTrain(.3)
            self.lbl82_txt.set(str(results[0]))
            self.lbl84_txt.set(str(results[1]))
        elif (txt_clicked2 == "All"):
            results = self.data.getLinearRegressionTrain(.3)
            self.lbl56_txt.set(str(results[0]))
            self.lbl58_txt.set(str(results[1]))
            results = self.data.getDecisionTreeTrain(.3)
            self.lbl62_txt.set(str(results[0]))
            self.lbl64_txt.set(str(results[1]))
            results = self.data.getKNNTrain(.3, 2)
            self.lbl72_txt.set(str(results[0]))
            self.lbl74_txt.set(str(results[1]))
            results = self.data.getNNTrain(.3)
            self.lbl82_txt.set(str(results[0]))
            self.lbl84_txt.set(str(results[1]))

    def graph(self):
        self.data.visualPreCleanGraph(self.clicked51.get())

    def test(self):

        self.found = StringVar()

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

        # self.lbl4 = Label(self.root, text='Hire Date')
        # self.lbl4.place(x=100, y=200)
        # t4complete = self.data.getUnique("Hire Date")
        # self.t4 = AutocompleteEntry(self.root, width=15, font=('Times', 12), completevalues=t4complete)
        # self.t4.place(x=200, y=200)

        # self.lbl5 = Label(self.root, text='Benefits Category')
        # self.lbl5.place(x=100, y=250)
        # self.t5 = Entry(bd=3, width=15, font=('Times', 12))
        # self.t5.place(x=200, y=250)

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

        # Results
        self.b10 = Button(self.root, text='Start', command=self.result)
        self.b10.place(x=100, y=400)
        options2 = [
            "Linear Regression",
            "Decision Trees",
            "KNN",
            "Neural Network"
        ]
        self.clicked2 = StringVar()
        self.clicked2.set("Linear Regression")
        self.opm7 = OptionMenu(self.root, self.clicked2, *options2)
        self.opm7.place(x=200, y=400)
        self.lbl10 = Label(self.root, text='Result')
        self.lbl10.place(x=100, y=450)
        self.t10 = Entry(self.root, textvariable=self.found)
        self.t10.place(x=200, y=450)

    def train(self):

        self.lbl100 = Label(self.root, text='Train')
        self.lbl100.place(x=500, y=10)

        # Results
        self.b50 = Button(self.root, text='Train', command=self.trainresult)
        self.b50.place(x=550, y=50)
        options5 = [
            "Linear Regression Train",
            "Decision Trees Train",
            "KNN Train",
            "Neural Network Train",
            "All"
        ]
        self.clicked50 = StringVar()
        self.clicked50.set("All")
        self.opm50 = OptionMenu(self.root, self.clicked50, *options5)
        self.opm50.place(x=600, y=50)

        # Graph
        # graphOptions = self.data.getNumericColumns()
        # self.clicked51 = StringVar()
        # self.clicked51.set(graphOptions[0])
        # self.opm51 = OptionMenu(self.root, self.clicked51, *graphOptions)
        # self.opm51.place(x=650, y=300)
        # self.lbl51 = Label(self.root, text='Select Graph')
        # self.lbl51.place(x=500, y=300)
        # self.btn52 = Button(self.root, text='Graph')
        ##self.b52.place(x=850, y=300)

        # Data Linear Regression
        self.lbl53 = Label(self.root, text='Linear Regression')
        self.lbl53.place(x=500, y=350)
        self.lbl54 = Label(self.root, text='Training Set Error')
        self.lbl54.place(x=500, y=375)
        self.lbl56_txt = StringVar()
        self.lbl56 = Label(self.root, textvariable=self.lbl56_txt)
        self.lbl56.place(x=500, y=400)
        self.lbl57 = Label(self.root, text='Test Set Error')
        self.lbl57.place(x=500, y=425)
        self.lbl58_txt = StringVar()
        self.lbl58 = Label(self.root, textvariable=self.lbl58_txt)
        self.lbl58.place(x=500, y=450)

        # Data Decision Trees
        self.lbl60 = Label(self.root, text='Decision Trees')
        self.lbl60.place(x=700, y=350)
        self.lbl61 = Label(self.root, text='Training Set Error')
        self.lbl61.place(x=700, y=375)
        self.lbl62_txt = StringVar()
        self.lbl62 = Label(self.root, textvariable=self.lbl62_txt)
        self.lbl62.place(x=700, y=400)
        self.lbl63 = Label(self.root, text='Test Set Error')
        self.lbl63.place(x=700, y=425)
        self.lbl64_txt = StringVar()
        self.lbl64 = Label(self.root, textvariable=self.lbl64_txt)
        self.lbl64.place(x=700, y=450)

        # Data KNN
        self.lbl70 = Label(self.root, text='KNN')
        self.lbl70.place(x=500, y=150)
        self.lbl71 = Label(self.root, text='Training Set Error')
        self.lbl71.place(x=500, y=175)
        self.lbl72_txt = StringVar()
        self.lbl72 = Label(self.root, textvariable=self.lbl72_txt)
        self.lbl72.place(x=500, y=200)
        self.lbl73 = Label(self.root, text='Test Set Error')
        self.lbl73.place(x=500, y=225)
        self.lbl74_txt = StringVar()
        self.lbl74 = Label(self.root, textvariable=self.lbl74_txt)
        self.lbl74.place(x=500, y=250)

        # Data Neural Network
        self.lbl80 = Label(self.root, text='Neural Network')
        self.lbl80.place(x=700, y=150)
        self.lbl81 = Label(self.root, text='Training Set Error')
        self.lbl81.place(x=700, y=175)
        self.lbl82_txt = StringVar()
        self.lbl82 = Label(self.root, textvariable=self.lbl82_txt)
        self.lbl82.place(x=700, y=200)
        self.lbl83 = Label(self.root, text='Test Set Error')
        self.lbl83.place(x=700, y=225)
        self.lbl84_txt = StringVar()
        self.lbl84 = Label(self.root, textvariable=self.lbl84_txt)
        self.lbl84.place(x=700, y=250)
