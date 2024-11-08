# Database Design Group Project!

![data-filtering](https://github.com/user-attachments/assets/8ca58e48-79db-4242-9f94-2736fd02e90a)


## 🧩 Project Overview
This project dives into the world of Kickstarter campaigns, analyzing and predicting project outcomes. Our team of four approached this as an end-to-end data solution: we structured the data, built a robust API, and integrated machine learning for predictive insights. Together, we’ve created a system that can store, manage, and utilize Kickstarter data to shed light on the factors that drive successful crowdfunding campaigns.

## 🎯 Problem Statement
Kickstarter projects range from viral successes to under-the-radar initiatives. We aimed to develop a comprehensive system that could:
1. Efficiently store and manage Kickstarter data.
2. Provide dynamic API access for CRUD operations.
3. Predict project outcomes based on historical trends and campaign attributes.

## 👥 Team Contributions

### Task 1: Database Schema Design
**Owner:** [Florent Magnifique Hirwa](https://github.com/fmhirwa/) 


**Objective:** Created a normalized Database Schema for the following [Unstructured Dataset for Software Companies](https://docs.google.com/spreadsheets/d/16uXnRa3jRmT5KK4tQCkCabE9j3nKsLKX/edit?gid=334424638#gid=334424638).

**Approach:**
- Analyzed the unstructured dataset to identify core entities and their relationships.
- Applied normalization techniques to minimize redundancy and improve data integrity.
- Developed an Entity-Relationship Diagram (ERD) to illustrate and validate the schema design.

**Deliverables:**
- A fully normalized database schema, optimized for efficient querying and storage.
- ERD with a comprehensive data dictionary for streamlined reference and understanding.

### Task 2: Database Implementation in MongoDB
**Owner:** [Aime Magnifique NDAYISHIMIYE](https://github.com/AIMEMAGNI)


**Objective:** Implement the database in MongoDB, leveraging its flexibility for storing and querying semi-structured data.

**Approach:**
- Crafted document structures for projects and categories to capture their nuances.
- Created collections with robust validation rules to maintain data integrity.
- Developed aggregation pipelines to support complex queries and optimize performance.

**Deliverables:**
- MongoDB collections for Kickstarter project data.
- Detailed data validation rules.
- Aggregation pipelines and indexing for efficient data retrieval.

### Task 3: RESTful API Development with FastAPI
**Owner:** [Pierrette Umutoniwase](https://github.com/Umutoniwasepie)  


**Objective:** Build a RESTful API that enables CRUD operations on Kickstarter data, supporting both users and downstream applications.

**Approach:**
- Set up FastAPI, ensuring an intuitive and efficient framework for API development.
- Designed and implemented endpoints for all CRUD operations:
  - `POST` for creating new projects
  - `GET` for retrieving project data
  - `PUT` for updates
  - `DELETE` for removals
- Focused on user-friendly error handling and comprehensive documentation to guide users.

  API LINK: **`https://kickstarter-api-3z5m.onrender.com`**

**Deliverables:**
- Fully functional API with Swagger documentation.
- CRUD endpoints with validation and error handling.
- Production-ready FastAPI application.

### Task 4: Machine Learning for Outcome Prediction
**Owner:** [Mohamed Ahmed Yasin](https://github.com/MohamedAYasin)  


**Objective:** Use machine learning to predict Kickstarter project outcomes based on campaign characteristics.

**Approach:**
- Created a data-fetching script to retrieve the latest project data from the [Kickstarter API](https://kickstarter-api.onrender.com).
- Preprocessed the data and loaded our trained model.
- Integrated prediction capabilities into the API, providing real-time project outcome forecasts.

**Deliverables:**
- Data-fetching script to keep predictions up-to-date. 
- Prediction pipeline that connects the model to the API.
- Performance analysis and documentation on model accuracy and usability.

**`https://kickstarter-api-3z5m.onrender.com/projects/latest`**

## 💡 Key Learnings
Our team gained invaluable experience in the full data pipeline, from raw data structuring to live API deployments and predictive modeling. Key takeaways include:
- **Data Schema Design**: Understanding the balance between normalization and performance, especially in document-based databases.
- **API Development**: Building flexible endpoints with FastAPI that can easily accommodate evolving data needs.
- **Machine Learning Integration**: Implementing a predictive model in a real-world setting and bridging it with an API for practical applications.

## 📊 Dataset
- Source: [Kaggle - Kickstarter Projects](https://www.kaggle.com/datasets/kemical/kickstarter-projects)
- Contains features that describe various aspects of Kickstarter campaigns, such as category, goal, and outcome.

  ## ⚙️ Technologies Used
- **Python**: Core programming language for data handling, API development, and model training.
- **Machine Learning Tools**: scikit-learn, pandas, matplotlib for building and visualizing the model.
- **MongoDB**: NoSQL database chosen for its scalability and document-based structure.
- **FastAPI**: Framework for building and documenting the API.


## 📈 Next Steps
Looking forward, we plan to expand this project by:
- Enhancing the model’s accuracy through feature engineering.
- Exploring additional data sources to enrich the prediction pipeline.

This project exemplifies our commitment to learning through collaboration, and we’re excited to continue refining and expanding it!

Thank you for being here! ❤️🙏



 -----------------         `©2024 The African Leadership University (ALU)`      ---------------------------------
