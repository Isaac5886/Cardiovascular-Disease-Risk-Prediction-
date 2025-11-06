# Cardiovascular-Disease-Risk-Prediction-


*This project uses machine learning to predict the likelihood of cardiovascular disease (CVD) by analyzing health, demographic, and lifestyle data. The aim is to enable early detection and support prevention efforts through accurate, data-driven risk assessment models.*

---

# 📊 Dataset Overview

This dataset, sourced from *Kaggle* on [Kaggle](https://www.kaggle.com/datasets/thedevastator/exploring-risk-factors-for-cardiovascular-diseas), contains health information for approximately *7,000 users*. It includes *13 features* plus the target variable (`cardio`), which indicates the presence or absence of cardiovascular disease. The features represent demographic, clinical, and lifestyle factors relevant to predicting cardiovascular risk.

---

# 🧠 Key Features

| Feature       | Description |
|---------------|-------------|
| `index`       | Row identifier (not used in modeling) |
| `id`          | Patient ID (can be ignored or used for tracking) |
| `age`         | Age in days *(convert to years for interpretation)* |
| `gender`      | 1 = Female, 2 = Male |
| `height`      | Height in centimeters |
| `weight`      | Weight in kilograms |
| `ap_hi`       | Systolic blood pressure |
| `ap_lo`       | Diastolic blood pressure |
| `cholesterol` | 1 = Normal, 2 = Above normal, 3 = Well above normal |
| `gluc`        | Glucose level: 1 = Normal, 2 = Above normal, 3 = Well above normal |
| `smoke`       | 1 = Smoker, 0 = Non-smoker |
| `alco`        | 1 = Alcohol consumer, 0 = Non-consumer 

---

`active` | 1 = Physically active, 0 = Inactive  
`cardio` | Target variable: 1 = Has cardiovascular disease, 0 = No disease

---

# 📊 Exploratory Data Analysis (EDA)

- *Age & Blood Pressure*: Older individuals tend to have higher blood pressure.
- *Cholesterol & Glucose*: Elevated levels are more common in those with cardiovascular disease.
- *BMI*: Overweight/obese users showed higher CVD risk.
- *Lifestyle*: Smokers and alcohol consumers showed slightly higher risk.
- *Target Balance*: `cardio` classes (0/1) are relatively balanced.

Basic visualizations like histograms, box plots, and correlation heatmaps were used to support these insights.

-----

# ⚙️ Feature Engineering

- Converted *age* from days (`age`) to years  
- Created *BMI* using weight and height: weight / (height/100)²  
- Categorized *blood pressure* using `ap_hi` (systolic) and `ap_lo` (diastolic) into clinical stages  
- Combined *smoke* and *alco* into a new *substance_use* feature  

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

- Best model: *Random Forest*
- Accuracy: *(add value)*  
- ROC-AUC: *(add value)*  

---

# 🚀 Streamlit App

An interactive web app is built using *Streamlit* to visualize and predict cardiovascular disease risk.

Features:
- Input patient data (age, gender, BP, cholesterol, etc.)
- Predict CVD risk (yes/no)
- Visualize feature importance

To Run:
```bash
streamlit run app.py
```


-----

# 🔗 Live Demo

Try the live demo here: [Streamlit App](https://your-app-url.streamlit.app)


----

# 📊 key Findings

- *Age*, *systolic BP*, *cholesterol*, and *BMI* were the top predictors.
- Smokers and alcohol users had a higher predicted risk.
- Physically active individuals showed lower risk on average.
- High glucose and cholesterol levels strongly correlated with CVD.
- The *Random Forest model* outperformed others in terms of accuracy and AUC.


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

This project is open-source and available under the MIT License.

---

# 🙋‍♂️ Author

*Your Name* – [GitHub Profile](https://github.com/yourusername)
```

---
