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

# Pull data from MongoDB collection
try:
    # Retrieve all documents from the collection
    documents = list(collection.find({}, {'_id': 0}))  # Exclude the MongoDB ID field

    # Convert to DataFrame
    data = pd.DataFrame(documents)

    # Save to CSV file
    csv_output_path = 'kickstarter_projects_for_ml.csv'
    data.to_csv(csv_output_path, index=False)
    print(f"Data saved to {csv_output_path} successfully!")
except Exception as e:
    print("An error occurred:", e)
