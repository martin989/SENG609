import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

file_name = "EnterFileNameHere"
# file_name = "C:\\Users\\Martin\\Desktop\\Masters\\Fall 2022 SENG-609\\Week 4\\Bank Customer Churn Prediction.csv"
df = pd.read_csv(file_name)
# print(df.head())

col_names = ["balance", "estimated_salary"]
features = df[col_names]

scaler = MinMaxScaler().fit(features.values)
features = scaler.transform(features.values)
scaled_features = pd.DataFrame(features, columns=col_names)
scaled_features.head()

print(scaled_features.describe())

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 5))

ax1.set_title('Before Scaling')
sns.kdeplot(df['balance'], ax=ax1)
sns.kdeplot(df['estimated_salary'], ax=ax1)
ax2.set_title('After Min-Max Scaling')
sns.kdeplot(scaled_features['balance'], ax=ax2)
sns.kdeplot(scaled_features['estimated_salary'], ax=ax2)
plt.show()
