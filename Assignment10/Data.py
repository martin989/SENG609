import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from warnings import simplefilter
from sklearn.neighbors import KNeighborsRegressor
from keras.layers import Dense, Dropout
from keras.models import Sequential
import os


# https://data.world/city-of-phoenix/2b41f4f8-fe6f-48d3-8097-ad44ee5bd616

class Data():
    def __init__(self, fileName):
        self.fileName = fileName
        self.df = pd.read_csv(self.fileName)
        self.df["Total Pay"] = self.df["Total Pay"].astype("float")
        # self.df["Benefits Category"] = self.df["Benefits Category"].astype("float")
        self.df["Department"] = self.df["Department"].astype("category")
        self.df["Job Title"] = self.df["Job Title"].astype("category")
        self.df["Full/Part Time"] = self.df["Full/Part Time"].astype("category")
        # self.df["Hire Date"] = self.df["Hire Date"].astype("category")
        # self.df["Benefits Category"] = pd.to_numeric(self.df["Benefits Category"], errors='coerce')
        self.df["Total Pay"].dropna()
        # self.df["Benefits Category"].dropna()
        self.df.drop_duplicates()
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.encodeData()

    def visualPreCleanGraph(self, column):
        if (column == "Total Pay Transformations"):
            self.testingDF["Total Pay"].plot(kind='hist', color='purple', edgecolor='black', figsize=(10, 7))
        else:
            self.df[column].plot(kind='hist', color='purple', edgecolor='black', figsize=(10, 7))
        plt.style.use('ggplot')
        plt.title('Distribution of ' + column, size=24)
        plt.xlabel(column, size=18)
        plt.ylabel('Frequency', size=18)
        plt.show()

    def getNumericColumns(self):
        df_num = self.df.select_dtypes(include=[np.number])
        lst = list(df_num.columns)
        lst.append("Total Pay Transformations")
        return lst

    def getDataFrame(self, jobTitle, department, hireDate, benefitsCategory, hours, enc):
        df = pd.DataFrame()
        df.insert(0, 'Job Title', jobTitle)
        df.insert(0, 'Department', department)
        df.insert(0, 'Hire Date', hireDate)
        df.insert(0, 'Benefits Category', benefitsCategory)
        df.insert(0, 'Full/Part Time', hours)
        new_row = {'Job Title': jobTitle, 'Department': department, 'Hire Date': hireDate,
                   'Benefits Category': benefitsCategory, 'Full/Part Time': hours
                   }
        df["Benefits Category"] = df["Benefits Category"].astype("float")
        df["Department"] = df["Department"].astype("category")
        df["Job Title"] = df["Job Title"].astype("category")
        df["Full/Part Time"] = df["Full/Part Time"].astype("category")
        df["Hire Date"] = df["Hire Date"].astype("category")
        df.loc[0] = new_row

        encoded = enc.transform(df[["Department", "Job Title", "Full/Part Time", "Hire Date"]]).toarray()
        df[enc.get_feature_names_out()] = encoded
        print(df.head())
        df.drop('Department', axis=1, inplace=True)
        df.drop('Job Title', axis=1, inplace=True)
        df.drop('Full/Part Time', axis=1, inplace=True)
        df.drop('Hire Date', axis=1, inplace=True)
        return df

    def getPredict(self, jobTitle, department, hireDate, benefitsCategory, hours, model):
        model = joblib.load(model)
        stand_scaler = joblib.load('scaler.joblib')
        encoder = joblib.load('encoder.joblib')
        df = self.getDataFrame(jobTitle, department, hireDate, benefitsCategory, hours, encoder)
        test_values = model.predict(df)
        predicted_value = test_values[0]
        value = stand_scaler.inverse_transform(predicted_value.reshape(-1, 1))
        return value[0]

    def getTrain(self, train_size, model, model_file_name):
        stand_scaler = joblib.load('scaler.joblib')
        y = self.testingDF["Total Pay"]
        X = self.testingDF.loc[:, self.testingDF.columns != 'Total Pay']
        xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=float(train_size))
        model.fit(xtrain, ytrain)
        joblib.dump(model, model_file_name)
        mse_train = mean_absolute_error(stand_scaler.inverse_transform(ytrain.values.reshape(1, -1)),
                                        stand_scaler.inverse_transform(model.predict(xtrain).reshape(1, -1)))
        mse_test = mean_absolute_error(stand_scaler.inverse_transform(ytest.values.reshape(1, -1)),
                                       stand_scaler.inverse_transform(model.predict(xtest).reshape(1, -1)))
        return [mse_train, mse_test]

    def getLinearRegressionTrain(self, train_size):
        regressor = LinearRegression()
        return self.getTrain(train_size, regressor, 'lin_model.pkl')

    def getDecisionTreeTrain(self, train_size):
        dtr = DecisionTreeRegressor()
        return self.getTrain(train_size, dtr, 'dec_model.pkl')

    def getKNNTrain(self, train_size, k):
        neigh = KNeighborsRegressor(n_neighbors=k)
        return self.getTrain(train_size, neigh, 'neigh.pkl')

    def getNNTrain(self, train_size):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        pd.options.mode.chained_assignment = None

        stand_scaler = joblib.load('scaler.joblib')
        self.testingDF.info()
        y = self.testingDF[["Total Pay"]]
        X = self.testingDF.drop(["Total Pay"], axis=1)
        xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=float(train_size))

        model = Sequential()
        # model.add(Dense(500, input_dim=xtrain.shape[1], activation='relu'))

        model.add(Dense(50, input_dim=xtrain.shape[1], activation='relu'))
        model.add(Dense(100, activation='sigmoid'))
        model.add(Dense(1, activation='relu'))
        model.compile(loss='mean_squared_error', optimizer='SGD')

        print("herereradsfsdfasdfa")
        model.fit(
            xtrain,
            ytrain,
            epochs=10,
            batch_size=10,
            shuffle=True,
            verbose=1
        )
        joblib.dump(model, 'nn_model.pkl')
        mse_train = mean_absolute_error(stand_scaler.inverse_transform(ytrain.values.reshape(1, -1)),
                                        stand_scaler.inverse_transform(model.predict(xtrain).reshape(1, -1)))
        mse_test = mean_absolute_error(stand_scaler.inverse_transform(ytest.values.reshape(1, -1)),
                                       stand_scaler.inverse_transform(model.predict(xtest).reshape(1, -1)))

        return [mse_train, mse_test]

    def encodeData(self):
        simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

        dfEnc = self.df.copy()
        enc = OneHotEncoder()

        encoded = enc.fit_transform(dfEnc[["Department", "Job Title", "Full/Part Time"]]).toarray()
        dfEnc[enc.get_feature_names_out()] = encoded

        self.testingDF = dfEnc.drop(["Department", "Job Title", "Full/Part Time"], axis=1)
        joblib.dump(enc, 'encoder.joblib')

        mmscaler = MinMaxScaler()
        cols = ['Total Pay']
        self.testingDF[cols] = mmscaler.fit_transform(self.testingDF[cols])
        joblib.dump(mmscaler, 'scaler.joblib')

    def getUnique(self, column):
        self.df.head()
        return self.df[column].unique()
