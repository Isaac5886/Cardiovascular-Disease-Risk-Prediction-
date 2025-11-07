# 🫀 Cardiovascular Disease Risk Prediction

-----

This project uses machine learning to predict the likelihood of cardiovascular disease (CVD) based on health, demographic, and lifestyle data. The goal is to assist early detection and prevention of CVD using data-driven models.

-----

# 🎯 Problem Statement

Cardiovascular disease (CVD) remains a leading cause of death globally, often progressing without clear symptoms until critical events occur. Early identification of high-risk individuals is crucial for timely intervention and prevention.

Traditional risk assessment methods require extensive clinical tests and expert analysis, which may not always be accessible or cost-effective. This project leverages machine learning to predict CVD risk using demographic, medical, and lifestyle data, aiming to enable early detection and support healthcare decisions.

---


# 📚 Table of Contents

- [Project Structure](#-project-structure)
- [Dataset Overview](#-dataset-overview)  
- [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)  
- [Feature Engineering](#-feature-engineering)  
- [Models Used](#-models-used)  
- [Evaluation Metrics](#-evaluation-metrics)  
- [Results](#-results)
- [Key Findings](#-key-findings)
- [Streamlit App](#-streamlit-app)  
- [Live Demo](#-live-demo)    
- [Requirements](#-requirements)  
- [License](#-license)  
- [Author](#-author)  
  

---

# 📁 Project Structure

```bash
cardio-risk-prediction/
│
├── data/                  # Raw or cleaned dataset(s)
│   └── cardio_data.csv
│
├── notebooks/             # Jupyter notebooks for EDA and modeling
│   └── eda.ipynb
│   └── model_training.ipynb
│
├── app/                   # Streamlit app files
│   └── app.py
│
├── models/                # Saved ML models (e.g., .pkl or .joblib)
│   └── model.joblib
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Files to ignore in Git
└── LICENSE                # License file
```

---

# 📊 Dataset Overview

This dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/thedevastator/exploring-risk-factors-for-cardiovascular-diseas), contains health information for approximately *7,000 users*. It includes *13 features* plus the target variable (`cardio`), representing whether a patient has cardiovascular disease.

---

# 🧠 Key Features

| Feature       | Description |
|---------------|-------------|
| `index`       | Row identifier|
| `id`          | Patient ID|
| `age`         | Age of the patient (in years)|
| `gender`      | Gender of the patient|
| `height`      | Height (cm) |
| `weight`      | Weight (kg) |
| `ap_hi`       | Systolic blood pressure |
| `ap_lo`       | Diastolic blood pressure |
| `cholesterol` | Cholesterol Level |
| `gluc`   | Glucose level |
| `smoke`       | Smoking Status (1 = yes, 0 = no) |
| `alco`        | Alcohol intake (1 = yes, 0 = no
| `active`   | Physical activity status (1 = active, 0 = Inactive) 
| `cardio` | Target variable: 1 = Has cardiovascular disease, 0 = No disease | 

---

# 📈 Exploratory Data Analysis (EDA)

Performed exploratory data analysis to understand the distributions  detect missing values, and observe relationship between features and the target variable.

-----

# ⚙️ Feature Engineering

- Converted *age* from days to years  
- Created *BMI* using weight and height (BMI = weight / (height/100)²) 
- Categorized *blood pressure* using `ap_hi` (systolic) and `ap_lo` (diastolic) into clinical stages  
- Combined *smoke* and *alco* into a new feature called *substance_use* 

---

# 🧠 Models Used

- Logistic Regression
- Random Forest
- XGBoost

---

# 🧪 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- ROC-AUC

---

# 📈 Results

The best performing model was *Random Forest* with: 
- Accuracy: *(add .value)*  
- ROC-AUC: *(add value)*  

---

# 💡 Key Findings

- Age, BMI, blood pressure, and substance use showed strong correlation with cardiovascular disease risk.  
- Lifestyle factors like physical activity had a significant impact on risk prediction.  

# 🖥️ Streamlit App

An interactive web app built with Streamlit is available to explore the prediction model.

To Run:
```bash
streamlit run app.py
```


-----

# 🔗 Live Demo

Try the live demo here: [Streamlit App](https://your-app-url.streamlit.app)


----


# 📦 Requirements

- Python 3.8+
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- xgboost (optional)
  
Install with:
```bash
pip install -r requirements.txt
```

---

# 📝 License

 MIT License.

---

# 🙋‍♂️ Author

*Agboola Isaac Oluwatomiwa:* – [GitHub Profile](https://github.com/yourusername)

---
