import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB credentials
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")

# Define the MongoDB URI
uri = f"mongodb+srv://{username}:{password}@cluster0.fxaek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(uri)
db = client['kickstarter_projects']  # Database name with underscores
collection = db['project_categories']  # Collection name with underscores

# Load only the first 5,000 rows of the CSV file with specific columns
csv_file_path = 'ks-projects-201612.csv'
selected_columns = ['ID', 'name', 'category', 'main_category', 'goal', 'state']
data = pd.read_csv(csv_file_path, usecols=selected_columns, nrows=5000, encoding='cp1252')

# Convert the DataFrame to a list of dictionaries
data_dict = data.to_dict(orient="records")

# Insert data into MongoDB
try:
    collection.insert_many(data_dict)
    print("Data uploaded successfully!")
except Exception as e:
    print("An error occurred:", e)
