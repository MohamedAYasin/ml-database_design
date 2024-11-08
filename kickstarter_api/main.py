from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")

# Connect to MongoDB
uri = f"mongodb+srv://{username}:{password}@cluster0.fxaek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['kickstarter_projects']
collection = db['project_categories']

app = FastAPI()

# Define data model for project creation
class Project(BaseModel):
    ID: int
    name: str
    category: str
    main_category: str
    goal: int
    state: str

# Helper function to convert ObjectId to string
def serialize_project(project):
    project['_id'] = str(project['_id'])
    return project

# Root endpoint with welcome message
@app.get("/")
async def root():
    return "Welcome to the Kickstarter Projects API. Use /docs endpoints to interact with the database."

# Fetch the latest project entry
@app.get("/projects/latest")
async def fetch_latest_project():
    latest_project = collection.find_one(sort=[("_id", -1)])
    if not latest_project:
        raise HTTPException(status_code=404, detail="No projects found.")
    return serialize_project(latest_project)

# Create a project
@app.post("/projects/")
async def create_project(project: Project):
    if collection.find_one({"ID": project.ID}):
        raise HTTPException(status_code=400, detail="Project with this ID already exists.")
    result = collection.insert_one(project.dict())
    return {"message": "Project created successfully.", "project_id": str(result.inserted_id)}

# Read a project by ID
@app.get("/projects/{project_id}")
async def read_project(project_id: int):
    project = collection.find_one({"ID": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return serialize_project(project)

# Update a project by ID
@app.put("/projects/{project_id}")
async def update_project(project_id: int, project: Project):
    if not collection.find_one({"ID": project_id}):
        raise HTTPException(status_code=404, detail="Project not found.")
    collection.update_one({"ID": project_id}, {"$set": project.dict()})
    return {"message": "Project updated successfully."}

# Delete a project by ID
@app.delete("/projects/{project_id}")
async def delete_project(project_id: int):
    result = collection.delete_one({"ID": project_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Project not found.")
    return {"message": "Project deleted successfully."}

