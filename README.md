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
