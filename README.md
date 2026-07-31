# 💼 Salary Prediction Model

A Machine Learning based application that predicts an estimated salary based on personal and professional attributes.

This project uses a trained regression model to predict salary using features such as age, gender, education level, job title, and years of experience.

## 🚀 Features

- Predicts estimated salary using Machine Learning
- Takes multiple career-related inputs
- Interactive user interface using Streamlit
- Fast salary predictions using a trained model

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

## 🤖 Machine Learning Model

- Algorithm: Random Forest Regression
- Problem Type: Regression

### Input Features

- Age
- Gender
- Education Level
- Job Title
- Years of Experience

### Output

- Predicted Salary

## 📊 Model Performance

The model achieved a high evaluation score on the test dataset.

**Model Score:** 0.99

Note:
Model performance depends heavily on the quality and distribution of training data. Further improvements can be made through better feature engineering, data preprocessing, and collecting more diverse data.

## 📦 Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 📂 Project Files

This repository contains:

- `app.py` — Streamlit application
- `salarypredictionmodel.joblib` — Trained Random Forest Regression model
- `requirements.txt` — Required Python packages

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Keep Model File Together

Make sure `app.py` and `rfsalary.joblib` are in the same folder.

### 3. Run Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## 🎯 Project Purpose

The purpose of this project is to demonstrate how Machine Learning regression models can be used to estimate salaries based on professional and educational attributes.
