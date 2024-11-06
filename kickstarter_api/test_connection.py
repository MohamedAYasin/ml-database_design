import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve MongoDB credentials
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")

# Define MongoDB URI
uri = f"mongodb+srv://{username}:{password}@cluster0.fxaek.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB and check the connection
try:
    client = MongoClient(uri)
    # Ping the server
    client.admin.command('ping')
    print("Connection to MongoDB was successful!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
