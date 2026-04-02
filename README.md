# 🎓 Student Dropout Risk Predictor

A machine learning web application that predicts whether a student will **Drop Out**, **Stay Enrolled**, or **Graduate** — based on academic, financial, and demographic factors.

> Built to help educational institutions identify at-risk students early and take timely action.

---

## 🔗 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://student-dropout-predictor-zrxsfxmbifcja6thbbf5dg.streamlit.app)

---

## 📌 Project Overview

| Detail | Value |
|---|---|
| Dataset Size | 4,424 students |
| Features | 35 academic, financial & demographic |
| Model | XGBoost Classifier |
| Accuracy | 77.4% |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```
student-dropout-predictor/
│
├── app.py                  # Streamlit UI — main entry point
│
├── model/
│   ├── train_model.py      # Model training & hyperparameter tuning
│   ├── predict.py          # Prediction logic (loads model & returns output)
│   └── model.pkl           # Saved trained XGBoost model
│
├── data/
│   ├── raw_data.csv        # Original dataset (4424 records, 35 features)
│   └── processed_data.csv  # Cleaned & encoded dataset
│
├── notebooks/
│   └── EDA.ipynb           # Exploratory Data Analysis notebook
│
├── utils/
│   └── preprocessing.py    # Reusable data cleaning & encoding functions
│
├── requirements.txt        # All dependencies
└── README.md               # You are here!
```

---

## 🔍 Key Findings

- 📉 Students with fewer than **5 approved subjects in Semester 2** are at high dropout risk
- 💸 **Unpaid tuition fees** is a strong standalone dropout indicator
- 📚 **Academic performance outweighs financial factors** in overall prediction weight
- 🎯 Early semester data is the most predictive — intervention works best in Semester 1–2

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Deployment | Streamlit, Streamlit Cloud |
| Version Control | Git, GitHub |

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/RupalagudiHaneef/student-dropout-predictor

# 2. Navigate into the folder
cd student-dropout-predictor

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 👤 Author

**Haneef Rupalagudi**
Python Developer & ML Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/haneef-rupalagudi-573b2b262)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/RupalagudiHaneef)
[![IEEE](https://img.shields.io/badge/IEEE-Published-green)](https://ieeexplore.ieee.org/document/10864175)
