import pandas as pd
from timeit import default_timer as timer
from keras.models import Sequential
from keras.layers import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib
from sklearn.metrics import mean_absolute_error
from ann_visualizer.visualize import ann_viz;

# Disable some useless pandas warnings to prevent some junk from showing up in the output window
pd.options.mode.chained_assignment = None

# Load our data set
df = pd.read_csv("house_data1.csv")

# Create the X and y arrays
X = df[["sq_feet", "num_bedrooms", "num_bathrooms"]]
y = df[["sale_price"]]

# Data needs to be scaled to  0 to 1 for the neural network to train correctly.
X_scaler = MinMaxScaler(feature_range=(0, 1))
y_scaler = MinMaxScaler(feature_range=(0, 1))

# The reason we need to create a separate scaler for the input values and the output values is that well want to be able to use them separately when we make real predictions with the model.
# Scale both the training inputs and outputs
X[X.columns] = X_scaler.fit_transform(X[X.columns])
y[y.columns] = y_scaler.fit_transform(y[y.columns])

# pandas dataframes into numpy arrays. becuase Tensor f does not support pandas datfrmaes
# Convert the inputs and outputs to numpy format so TensorFlow doesn't complain
X = X.to_numpy()
y = y.to_numpy()

# Split the data set in a training set (75%) and a test set (25%)
# Its important to do this after we scale the data to make sure that the training and test sets are scaled exactly the same way.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Create a Neural Network model

# Keras has different APIs for defining neural networks that we can choose between.
# The most commonly used is the Sequential API.
# The Sequential API is the version in which we define it one layer at a time, in sequence. It's the easiest way to do it, so that's what we'll use too.
model = Sequential()
# So far, we've only learned about the simplest kind of neural network layer where every node in the layer is connected to every node in the following layer.
# These are called dense layers because the nodes are densely connected.


# This single line actually will create two layers,  a three-node input layer and a 50-node hidden layer.
# This is because the first layer in Keras has a special input_shape parameter.
# This tells Keras that we want three input nodes in the neural network.
# Instead of declaring the input layer on its own line, this is how Keras specifies the size of the input layer.
model.add(Dense(50, input_dim=3, activation='relu'))
# Earlier, we talked about hidden layers with four nodes. But in real life, we'll often use hundreds of nodes in a single layer.
model.add(Dense(50, activation='relu'))
# relu = rectified linear unit , i.e. only share if you have positive value 
model.add(Dense(50, activation='relu'))

model.add(Dense(50, activation='relu'))

# This is the output layer, 1 value is the predicted value of the house linear means no activation
model.add(Dense(1, activation='linear'))

# we need to tell Keras to construct the neural network inside of TensorFlow for us.
model.compile(loss='mean_squared_error', optimizer='SGD')
# LOSS  for other loss functions check out Keras API, for continuous values MSE is good
# Optimizer stochastic gradient descent
# Train the model
# keras tries to imitate Sci-kit so t also calls it model.fit()

start = timer()
fullstart = start
model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=8,
    shuffle=True,
    verbose=2
)
end = timer()
print("The NN model training took: %.3f ms" % (1000 * (end - fullstart)))
# paramters

# 1-epochs is how many times we will loop through the entire training dataset before ending the gradient descent training process.
# 2 batch_size controls how many training examples are considered at once during each gradient descent update pass.
# 3 shuffle=True tells Keras to randomize the order of the input data it sees. 
# This is super important. You always want to randomize the order of your training data unless you know for sure that you have it stored in random order already.
# 4  verbose just controls how much Keras prints on the screen during the training process.
# Setting it to 2 makes it print less output.


# Save the scalers to files so we can use it to pre-process new data later
joblib.dump(X_scaler, "X_scaler.pkl")
joblib.dump(y_scaler, "y_scaler.pkl")

# Save the trained model to a file so we can use it to make predictions later
model.save("house_value_model.h5")

# Report how well the model is performing
print("Model training results:")
# Report mean absolute error on the training set in a value scaled back to dollars so it's easier to understand.
predictions_train = model.predict(X_train, verbose=0)

mse_train = mean_absolute_error(
    y_scaler.inverse_transform(predictions_train),
    y_scaler.inverse_transform(y_train)
)
print(f" - Training Set Error: {mse_train}")

# Report mean absolute error on the test set in a value scaled back to dollars so it's easier to understand.
predictions_test = model.predict(X_test, verbose=0)

mse_test = mean_absolute_error(
    y_scaler.inverse_transform(predictions_test),
    y_scaler.inverse_transform(y_test)
)
print(f" - Test Set Error: {mse_test}")

# ann_viz(model, title="My first neural network")
