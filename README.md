# MLops-Project
Welcome to the MLops-Project repository! This project showcases an end-to-end machine learning pipeline, including data management, model development, API creation, and deployment. Below, you'll find instructions on how to navigate and use this project.

# Project Overview
This project demonstrates the following key components:

Environment Setup: Setting up a Conda environment for machine learning development and installing necessary packages.

Repositories: Managing code using Git and integrating GitHub Actions for continuous integration.

Data: Downloading and cleaning the dataset for training the machine learning model.

Model: Developing a machine learning model and writing unit tests for model functions.

API Creation: Creating a RESTful API using FastAPI for making predictions with the trained model.

API Deployment: Deploying the API to Heroku for live access.

# Environment Set up
* Download and install conda if you don’t have it already.
    * Use the supplied requirements file to create a new environment, or
    * conda create -n [envname] "python=3.8" scikit-learn pandas numpy pytest jupyter jupyterlab fastapi uvicorn -c conda-forge
    * Install git either through conda (“conda install git”) or through your CLI, e.g. sudo apt-get git.

# Data
* census.csv is the initial data and the cleaned data is census_cleaned.csv

# Model
* We used RandomForestClassifier to train our model.

# API Creation
*  We created a RESTful API using FastAPI which implements:
    * GET on the root giving a welcome message.
    * POST that does model inference.

# API Deployment
* We deployed this repository in render
* https://mlops-project.onrender.com/
  
