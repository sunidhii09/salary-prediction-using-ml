# Salary Prediction Application

## Overview

The Salary Prediction Application is a web-based tool that predicts the salary of an individual based on various factors such as age, experience, job title, gender, and education level. The application uses a machine learning model hosted on a FastAPI backend to generate the salary predictions.

## Features

- **User Input Form**: Users can input their details such as age, years of experience, job title, gender, and education level.
- **Salary Prediction**: The application processes the input data through a machine learning model and predicts the expected salary.
- **Real-time Feedback**: The application provides immediate feedback for incorrect inputs.

## Prerequisites

- Python 3.x
- Docker
- Docker Compose (optional, but recommended)

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/salary-prediction.git
    cd salary-prediction
    ```

2. **Install Python dependencies**:

    Create a virtual environment and install the required packages:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the FastAPI backend**:

    ```bash
    uvicorn backend.main:app --reload
    ```

    The backend server will start on `http://localhost:8000`.

4. **Open the frontend**:

    Open the `frontend/index.html` file in your web browser.

### Using Docker

1. **Build the Docker image**:

    ```bash
    docker build -t my-fastapi-app .
    ```

2. **Run the Docker container**:

    ```bash
    docker run -p 8000:8000 my-fastapi-app
    ```

    The application will be accessible at `http://localhost:8000`.

## How to Use

1. **Open the application** in your web browser (e.g., by opening `frontend/index.html` or accessing `http://localhost:8000` if using Docker).

2. **Fill out the form** with the required information:
    - Age (between 18 and 75)
    - Years of experience
    - Job title (select from the dropdown)
    - Gender
    - Education level (select from the dropdown)

3. **Click on "Predict Salary"**. The application will display the predicted salary based on the provided information.

4. **Error Handling**: If the age or years of experience entered is outside the specified range, a message will be displayed asking to enter valid details.

