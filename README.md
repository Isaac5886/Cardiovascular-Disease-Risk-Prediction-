

# 🫀 Cardiovascular Disease Risk Prediction Using Machine Learning 

-----

This project uses machine learning to predict the likelihood of cardiovascular disease (CVD) based on health, demographic, and lifestyle data. The goal is to assist early detection and prevention of CVD using data-driven models.

-----

# 🎯 Problem Statement

Cardiovascular disease (CVD) remains a leading cause of death globally, often progressing without clear symptoms until critical events occur. Early identification of high-risk individuals is crucial for timely intervention and prevention.

Traditional risk assessment methods require extensive clinical tests and expert analysis, which may not always be accessible or cost-effective. This project leverages machine learning to predict CVD risk using demographic, medical, and lifestyle data, aiming to enable early detection and support healthcare decisions.

---


# 📚 Table of Contents

- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
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
- [Contact](#-contact)
  

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

# ▶️ Getting Started 

1. *Clone the repository:*

```bash
git clone https://github.com/Isaac5886/Cardiovascular-Disease-Risk-Prediction-.git
cd Cardiovascular-Disease-Risk-Prediction-
```

2. *Install the dependencies:*

```bash
pip install -r requirements.txt
```

3. *Run the Streamlit app:*

```bash
streamlit run app.py
```

4. *Open your browser and go to:*

```
http://localhost:8501
```


---

# 📊 Dataset Overview

This dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/thedevastator/exploring-risk-factors-for-cardiovascular-diseas), contains health information for approximately *7,000 users*. It includes *14 features* plus the target variable (`cardio`), representing whether a patient has cardiovascular disease.

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
- Decision Tree Classifier 
- Random Forest classifier
- XGBoost Classifier 
- KNeighborsClassifier 
- Gaussian naive Bayes 

---

# 🧪 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1 score 
- ROC-AUC

---

# 📈 Results

The best performing model was *XGBoost Classifier* with: 
- Accuracy: *0.73*  
- Precision: *0.75*
- Recall: *0.69*
- F1 score: *0.72*
- ROC-AUC: *0.79*  

# Confusion Matrix

|               | Predicted No Disease | Predicted Disease |
|---------------|----------------------|-------------------|
| *Actual No Disease* | 5360                 | 1578              |
| *Actual Disease*    | 2118                 | 4675              |


- *True Negatives (TN):* 5360  
- *False Positives (FP):* 1578  
- *False Negatives (FN):* 2118  
- *True Positives (TP):* 4675


# 🗣️ *Interpretation:*

This confusion matrix shows how well the model classified individuals:
- *True Positives (4675):* Correctly predicted as having CVD.
- *True Negatives (5360):* Correctly predicted as not having CVD.
- *False Positives (1578):* Incorrectly predicted as having CVD.
- *False Negatives (2118):* Missed cases of actual CVD.

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

Try the live demo here: [Streamlit App](https://vascular.streamlit.app/)


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

*Agboola Isaac Oluwatomiwa:* - https://github.com/Isaac5886

---

# 📞 Contact

If you have any questions or want to reach out, feel free to contact me:

- *Name:* Agboola Isaac Oluwatomiwa  
- *Email:* agboolaisaac83@gmail.com  
- *Phone:* +234 808 251 7406  
- *GitHub:* [Isaac5886](https://github.com/Isaac5886)
---
