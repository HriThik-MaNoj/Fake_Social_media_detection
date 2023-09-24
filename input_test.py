import pandas as pd
import numpy as np
import keras
from keras.models import Sequential, model_from_json
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Load the trained model and weights
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

# Function to preprocess user input
def preprocess_input(input_link):
    # Your preprocessing code here, for example, extract features from the input link
    # Replace this with your actual preprocessing logic
    features = [0, 0, 0, 0, 0, 0, 0, 0]  # Placeholder values
    return features

# Function to predict if the profile is fake or not
def predict_fake_profile(input_features):
    input_features = np.array(input_features).reshape(1, -1)  # Reshape for prediction
    prediction = loaded_model.predict(input_features)
    return prediction[0]

# User input for the social media profile link
user_input_link = input("Enter the social media profile link: ")
input_features = preprocess_input(user_input_link)
prediction = predict_fake_profile(input_features)

if prediction > 0.5:
    print("The social media profile is predicted to be fake.")
else:
    print("The social media profile is predicted to be genuine.")

