# Task 4 - Create a Script to Fetch Data for Prediction

## Overview

In this task, I implemented two main steps:

1. **Fetching Data from Kickstarter API**: A script was created to fetch the latest Kickstarter project data from an API hosted at [Kickstarter API](https://kickstarter-api.onrender.com).
2. **Prediction and Model Evaluation**: Using a pre-trained model, I processed the fetched data to make predictions about the outcome of Kickstarter projects, evaluating the model's performance by calculating its accuracy.

## 1. Fetching Data for Prediction

To fetch the latest Kickstarter project data, I utilized the **Kickstarter API**, which provides various details about Kickstarter projects such as the project outcome (`successful`, `failed`, `canceled`), categories, and other related features.

The script sends a request to the API and receives data in JSON format, which is then converted into a Pandas DataFrame for further processing. This data includes project-specific information such as the project outcome, categories, and other details necessary for prediction.

## 2. Model Prediction and Evaluation

Once the data is fetched and pre-processed, it is passed through a pre-trained machine learning model that was previously trained on Kickstarter project data. This model predicts the likely outcome of a project (whether it will be successful, failed, or canceled).

### Steps Involved:
- **Load the Pre-Trained Model**: The model, which was saved as a `.pkl` file, is loaded into the environment.
- **Prepare the Data for Prediction**: The fetched data is pre-processed by encoding categorical variables and splitting the data into features and the target variable.
- **Make Predictions**: The pre-processed data is passed through the model to predict the outcome of each Kickstarter project.
- **Evaluate Model Performance**: The model's accuracy is calculated, and the results are displayed with a classification report and a confusion matrix.

### Key Performance Metrics:
- **Accuracy**: The model’s overall prediction accuracy is computed and displayed.
- **Classification Report**: A report detailing precision, recall, and F1 score for each predicted class.
- **Confusion Matrix**: A matrix that shows the true positive, false positive, true negative, and false negative predictions for a more detailed performance analysis.

## Conclusion

This task demonstrates how to:
1. Fetch real-time Kickstarter project data using the Kickstarter API.
2. Use the pre-trained model to make predictions about the success or failure of Kickstarter projects.
3. Evaluate the model’s performance using various metrics.

## Technologies Used:
- **Python**: For scripting and data manipulation.
- **Scikit-learn**: For the machine learning model and evaluation.
- **Requests**: For fetching data from the Kickstarter API.
- **Pandas**: For data processing and manipulation.
- **Matplotlib/Seaborn**: For visualizing model evaluation results like confusion matrix.

## Next Steps:
- Improve data preprocessing to handle edge cases (e.g., missing or incomplete data).
- Explore deploying the model for real-time predictions on new Kickstarter projects.
