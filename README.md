# Student Dropout Risk Predictor

A machine-learning web application that estimates whether a student is likely to **drop out, remain enrolled, or graduate** using academic, financial, and demographic information.

The project demonstrates an end-to-end ML workflow: data preparation, model training, evaluation, and deployment through Streamlit.

## Live application

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://student-dropout-predictor-zrxsfxmbifcja6thbbf5dg.streamlit.app)

## Project at a glance

| Item | Details |
|---|---|
| Dataset | 4,424 student records |
| Input features | 35 |
| Model | XGBoost Classifier |
| Reported accuracy | 77.4% |
| Application | Streamlit |
| Language | Python |

*The accuracy shown is the result reported for this project; performance can vary with data splits and evaluation conditions.*

## Why this project?

Student attrition can affect learners and educational institutions. This application explores how historical student data can support early identification of students who may need additional academic or administrative support. Predictions should be treated as decision-support signals, not as final judgments about individual students.

## Technology stack

- **Python** — application and model workflow
- **Pandas, NumPy** — data handling and preprocessing
- **Scikit-learn, XGBoost** — model development and evaluation
- **Matplotlib, Seaborn** — exploratory analysis and visualization
- **Streamlit** — interactive web application
- **Git, GitHub** — version control

## Repository structure

```text
student-dropout-predictor/
├── app.py
├── model/
│   ├── train_model.py
│   ├── predict.py
│   └── model.pkl
├── data/
│   ├── raw_data.csv
│   └── processed_data.csv
├── notebooks/
│   └── EDA.ipynb
├── utils/
│   └── preprocessing.py
├── requirements.txt
└── README.md
```

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/RupalagudiHaneef/student-dropout-predictor.git
   cd student-dropout-predictor
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

   Windows:
   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   streamlit run app.py
   ```

## Responsible use

- A model prediction is an estimate, not a certainty.
- Use predictions alongside human review and relevant context.
- Check data quality and model performance before using the system in a real institutional setting.
- Do not use the output as the sole basis for consequential decisions about a student.

## Author

**Haneef Rupalagudi**  
Python Developer | AI/ML Enthusiast

- [GitHub](https://github.com/RupalagudiHaneef)
- [LinkedIn](https://linkedin.com/in/haneef-rupalagudi-573b2b262)
- [IEEE Xplore publication](https://ieeexplore.ieee.org/document/10864175)

---

If you find this project useful, feel free to explore the code and share constructive feedback.
