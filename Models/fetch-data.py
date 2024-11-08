'''This script Fetches a Kickstarter Project entry by project ID from the database and makes Predictions with it'''

import requests
import joblib
import pandas as pd
import os

# Prompt the user to enter a project ID
project_id = input("Please enter the project ID: ")

# Define the function to fetch the project entry by ID
def fetch_project_by_id(project_id):
    api_url = f"https://kickstarter-api.onrender.com/projects/{project_id}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        project_entry = response.json()
        return project_entry
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Fetch the project entry by the user-provided ID
project_entry = fetch_project_by_id(project_id)

# Continue only if project_entry is available
if project_entry:
    print(f"Fetched Project Entry: \n{project_entry}")
else:
    print("Try again. No Data is currently available on this ID.")