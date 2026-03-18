# Student Dropout Risk Predictor

A machine learning web application that predicts whether a student will 
Drop Out, Stay Enrolled, or Graduate based on academic and financial factors.

## Live App
[Click here to open the app](https://student-dropout-predictor-zrxsfxmbifcja6thbbf5dg.streamlit.app)

## Project Overview
- Dataset: 4424 students, 35 features
- Model: XGBoost Classifier
- Accuracy: 77.4%

## Key Findings
- Students with 2nd semester approved subjects below 5 are at high dropout risk
- Unpaid tuition fees is a strong dropout indicator
- Academic performance outweighs financial factors in prediction

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn, XGBoost
- Streamlit

## How to Run Locally
pip install -r requirements.txt
streamlit run app.py

## Author
Haneef Rupalagudi