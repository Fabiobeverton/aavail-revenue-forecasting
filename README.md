AAVAIL Revenue Forecasting – Capstone Project

This repository contains the final submission for the IBM AI Workflow Architect Capstone Project. The project implements a time-series forecasting solution for AAVAIL's business case, focused on predicting future revenue across countries.

🔧 Project Structure

.
├── api.py                  # Flask API for serving predictions
├── model.py                # Model loading and prediction logic
├── ingest_data.py          # Data ingestion logic
├── notebook_capstone.ipynb # Full EDA, modeling, and evaluation
├── test_api.py             # Unit tests for API
├── test_model.py           # Unit tests for model logic
├── test_logging.py         # Unit tests for logging
├── run_tests.sh            # Script to run all unit tests at once
├── Dockerfile              # Containerization of API
├── requirements.txt        # Python dependencies

🎓 Objectives

Perform exploratory data analysis (EDA) with visualizations

Engineer time-series features

Train and evaluate multiple forecasting models

Compare model vs baseline using performance plots

Build a REST API to serve model predictions

Implement unit testing (model, API, logging)

Containerize the project using Docker

Provide monitoring and logging mechanism

📊 Models Compared

Baseline model: Simple moving average

Model 1: Linear regression

Model 2: ARIMA or Prophet (depending on experiment)

Model performance was evaluated using MAE, RMSE, and trend tracking over 500+ days.

⚙️ How to Run Locally

1. Build Docker image

docker build -t aavail-api .

2. Run the container

docker run -p 5000:5000 aavail-api

API will be available at http://localhost:5000

💹 API Usage

Endpoint

Description

/predict?country=USA

Predict for a specific country

/predict_all

Predict for all countries combined

Input format and response schema are shown in the notebook.

📊 Monitoring & Logging

Logging is handled via Python logging module

Logs include timestamp, inputs, and model outputs

Stored in /logs/ folder inside the container or local project

🔧 Unit Testing

Run all tests with a single command:

bash run_tests.sh

Tests include:

API functionality

Model input/output

Logging checks

Edge case handling

👀 Visualizations

EDA time-series plots (daily revenue, views, purchases)

Forecasts vs actuals

Model comparison graphs

All visuals are included in notebook_capstone.ipynb

🚀 Deployment Ready

This project is containerized, modular, tested, and ready for deployment.

Peer reviewers are welcome to clone the repo, build the image, run the API, and inspect the tests and results. All core workflow components from ingestion to model to API and validation are covered.

Submitted by: Fabio EvertonIBM AI Workflow Architect CapstoneDate: August 2025

