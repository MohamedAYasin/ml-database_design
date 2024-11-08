"""This script Fetches the Latest Kickstarter Project entry from the database and makes Predictions with it"""

import requests
import joblib
import pandas as pd
import os

# Define the API URL for fetching the latest entry
api_url = "https://kickstarter-api-3z5m.onrender.com/projects/latest"

# Step 1: Fetch the latest entry from the API
try:
    response = requests.get(api_url)
    response.raise_for_status()
    latest_entry = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    latest_entry = None

# Step 2: Continue only if latest_entry is available
if latest_entry:
    print(f"Fetched Latest Entry: \n{latest_entry}")

    # Define the path to the model file (Update this path as needed)
    model_path = 'kickstarter_model.pkl'  # Specify the path to your model here

    # Load the trained model
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        print(f"Model file not found at {model_path}")
        model = None

    if model:
        # Convert the fetched entry into a DataFrame for preprocessing
        data_df = pd.DataFrame([latest_entry])

        # Select and preprocess relevant features
        expected_columns = ['goal', 'name', 'category', 'main_category', 'state', 'backers', 'pledged', 'usd_pledged']

        # Ensure all expected columns are present
        for col in expected_columns:
            if col not in data_df.columns:
                data_df[col] = 0

        data_df = data_df[expected_columns]

        # Handle categorical variables
        data_df = pd.get_dummies(
            data_df, columns=['name', 'category', 'main_category', 'state'], drop_first=True
        )

        # Align the DataFrame with the model's expected input features
        model_features = model.feature_names_in_
        for feature in model_features:
            if feature not in data_df.columns:
                data_df[feature] = 0

        data_df = data_df[model_features]

        # Convert to input format
