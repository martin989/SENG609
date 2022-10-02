import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression


# https://data.world/city-of-phoenix/2b41f4f8-fe6f-48d3-8097-ad44ee5bd616

class Data():
    def __init__(self, fileName):
        self.fileName = fileName
        self.df = pd.read_csv(self.fileName)
        self.df["Total Pay"] = self.df["Total Pay"].astype("float")
        self.df["Benefits Category"] = self.df["Benefits Category"].astype("float")
        self.df["Department"] = self.df["Department"].astype("category")
        self.df["Job Title"] = self.df["Job Title"].astype("category")
        self.df["Full/Part Time"] = self.df["Full/Part Time"].astype("category")
        self.df["Hire Date"] = self.df["Hire Date"].astype("category")
        self.df["Benefits Category"] = pd.to_numeric(self.df["Benefits Category"], errors='coerce')
        self.df["Total Pay"].dropna()
        self.df["Benefits Category"].dropna()
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
        encoder = enc

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

    def getLinearRegression(self, jobTitle, department, hireDate, benefitsCategory, hours):
        model = joblib.load('lin_model.pkl')
        stand_scaler = joblib.load('scaler.joblib')
        encoder = joblib.load('encoder.joblib')
        df = self.getDataFrame(jobTitle, department, hireDate, benefitsCategory, hours, encoder)
        print(df.head())

        test_values = model.predict(df)
        predicted_value = test_values[0]
        value = stand_scaler.inverse_transform(predicted_value.reshape(-1, 1))
        return value[0]

    def getLinearRegressionTrain(self, train_size):
        y = self.testingDF["Total Pay"]
        X = self.testingDF.loc[:, self.testingDF.columns != 'Total Pay']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(train_size))
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        joblib.dump(regressor, 'lin_model.pkl')

        mse_train = mean_absolute_error(y_train, regressor.predict(X_train))
        mse_test = mean_absolute_error(y_test, regressor.predict(X_test))
        return [mse_train, mse_test]

    def getDecisionTree(self, jobTitle, department, hireDate, benefitsCategory, hours):
        model = joblib.load('dec_model.pkl')
        stand_scaler = joblib.load('scaler.joblib')
        encoder = joblib.load('encoder.joblib')
        df = self.getDataFrame(jobTitle, department, hireDate, benefitsCategory, hours, encoder)
        test_values = model.predict(df)
        predicted_value = test_values[0]
        value = stand_scaler.inverse_transform(predicted_value.reshape(-1, 1))
        return value[0]

    def getDecisionTreeTrain(self, train_size):
        y = self.testingDF["Total Pay"]
        X = self.testingDF.loc[:, self.testingDF.columns != 'Total Pay']
        xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=float(train_size))
        dtr = DecisionTreeRegressor()
        dtr.fit(xtrain, ytrain)
        joblib.dump(dtr, 'dec_model.pkl')
        mse_train = mean_absolute_error(ytrain, dtr.predict(xtrain))
        mse_test = mean_absolute_error(ytest, dtr.predict(xtest))
        return [mse_train, mse_test]

    def encodeData(self):
        dfEnc = self.df.copy()
        enc = OneHotEncoder()

        encoded = enc.fit_transform(dfEnc[["Department", "Job Title", "Full/Part Time", "Hire Date"]]).toarray()
        dfEnc[enc.get_feature_names_out()] = encoded
        self.testingDF = dfEnc.drop(["Department", "Job Title", "Full/Part Time", "Hire Date"], axis=1)
        joblib.dump(enc, 'encoder.joblib')

        mmscaler = MinMaxScaler()
        cols = ['Total Pay']
        self.testingDF[cols] = mmscaler.fit_transform(self.testingDF[cols])
        joblib.dump(mmscaler, 'scaler.joblib')

    def getUnique(self, column):
        self.df.head()
        return self.df[column].unique()
