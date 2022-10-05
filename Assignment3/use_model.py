# from sklearn.externals
import joblib

# Load our trained model
linear_model = joblib.load('linear_house_value_model.pkl')
decision_model = joblib.load('decision_house_value_model.pkl')
# Define the house that we want to value (with the values in the same order as in the training data)
house_1 = [
    2500,  # Size in Square Feet
    3,  # Number of Bedrooms
    2,  # Number of Bathrooms
]
# scikit-learn assumes you want to predict the values for multiple of houses atonce, so it expects an array.
# We only want to estimate the value of a single house, so there will only be oneitem in our array.
homes = [
    house_1
]
# Make a prediction for each house in the homes array (we only have one)
linear_home_values = linear_model.predict(homes)
decision_home_values = decision_model.predict(homes)
# Since we are only predicting the price of one house, grab the first prediction returned
linear_predicted_value = linear_home_values[0]
decision_predicted_value = decision_home_values[0]
# Print the results
print("Linear Regression House details:")
print(f"- {house_1[0]} sq feet")
print(f"- {house_1[1]} bedrooms")
print(f"- {house_1[2]} bathrooms")
print(f"Estimated value: ${linear_predicted_value:,.2f}")

print("Decision Tree House details:")
print(f"- {house_1[0]} sq feet")
print(f"- {house_1[1]} bedrooms")
print(f"- {house_1[2]} bathrooms")
print(f"Estimated value: ${decision_predicted_value:,.2f}")
