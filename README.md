# Calorie Burnt Prediction 🏋️‍♂️🔥

This repository contains a Machine Learning project that predicts the number of calories burned during physical activities based on biometric and motion data. The goal is to help users better understand their energy expenditure using data-driven methods.

## 📌 Project Overview

Calorie tracking plays a vital role in fitness, diet, and health monitoring. This project utilises various supervised learning algorithms to estimate calorie expenditure from a dataset containing biometric and physical activity parameters like age, gender, height, weight, duration, heart rate, and body temperature.

## 📁 Dataset

- **Source**: The dataset used in this project is a combination of two CSV files: `calories.csv` and `exercise.csv`, containing details about the person's physical activity and corresponding calories burnt.
- **Features Used**:
  - `Gender`
  - `Age`
  - `Height`
  - `Weight`
  - `Duration`
  - `Heart_Rate`
  - `Body_Temp`
  - `Calories` (Target)

## ⚙️ Tech Stack

- **Language**: Python
- **Libraries**:
  - `pandas` – Data manipulation
  - `numpy` – Numerical operations
  - `seaborn`, `matplotlib` – Data visualization
  - `scikit-learn` – ML models and preprocessing

## 🧠 Models Used

- Linear Regression
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor

## 🔍 Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

## 📊 Results Summary

After training and evaluating different regression models, the Random Forest Regressor yielded the best performance with high accuracy and low error metrics.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Shivaanshtyagii/calories_burned.git
   cd calories_burned
