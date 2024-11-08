# Kickstarter Projects API

This is a FastAPI project designed to perform CRUD operations on a Kickstarter dataset stored in MongoDB Atlas. The API allows you to create, read, update, and delete Kickstarter project records.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Environment Setup](#environment-setup)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## 📌 Project Overview

This project involves building RESTful API endpoints using FastAPI for a MongoDB database containing Kickstarter project data. The project uses MongoDB Atlas to store and manage the data.

## 🛠 Technologies Used

- **Python** (v3.11.1)
- **FastAPI** - For building the API
- **MongoDB Atlas** - For the NoSQL database
- **pymongo** - For interacting with MongoDB
- **python-dotenv** - For managing environment variables
- **Uvicorn** - For running the FastAPI server

---

## ⚙️ Environment Setup

### Prerequisites
- Python 3.11.1 or higher
- MongoDB Atlas account

---

## 🔄 API Endpoints

Here’s a list of the available endpoints:

1. **Create a New Project**
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "ID": 12345,
       "name": "Sample Project",
       "category": "Technology",
       "main_category": "Tech",
       "goal": 5000,
       "state": "successful"
     }
     ```
2. **Get/Fetch the latest entry**
   - **Method**: `GET`
   - **URL**: `/projects/latest`
     
3. **Get a Project by ID**
   - **Method**: `GET`
   - **URL**: `/projects/{project_id}`

4. **Update a Project**
   - **Method**: `PUT`
   - **URL**: `/projects/{project_id}`
   - **Request Body**:
     ```json
     {
       "name": "Updated Project Name",
       "category": "Art",
       "main_category": "Creative",
       "goal": 10000,
       "state": "failed"
     }
     ```

5. **Delete a Project**
   - **Method**: `DELETE`
   - **URL**: `/projects/{project_id}`

---

## 🌐 Deployment 

This API is deployed on **Render**. Access the live API at:  [https://kickstarter-api.onrender.com](https://kickstarter-api-3z5m.onrender.com)

---

## ✨ Contributing

This part of the project was handled by **Pierrette Umutoniwase**, who was responsible for the **API development** using FastAPI, implementing CRUD operations, and ensuring smooth interaction with the MongoDB database.
