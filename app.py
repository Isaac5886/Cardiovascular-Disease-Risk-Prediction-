import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="Heart Disease Risk Assessment",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e3a8a;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
        padding-bottom: 10px;
        border-bottom: 3px solid #3b82f6;
    }
    h2 {
        color: #1e40af;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 500;
    }
    h3 {
        color: #2563eb;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        font-size: 16px;
        font-weight: 600;
        padding: 14px 40px;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    .info-box {
        background-color: #eff6ff;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        margin: 20px 0;
    }
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    .debug-box {
        background-color: #fff7ed;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #f59e0b;
        margin: 10px 0;
        font-family: monospace;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)


# Load model
@st.cache_resource
def load_model():
    model = joblib.load('best_model_lr.pkl')
    return model

model = load_model()


# Professional sidebar
with st.sidebar:
    st.markdown("## 📊 Clinical Decision Support")
    st.markdown("---")
    
    st.markdown("### About This Tool")
    st.markdown("""
    This clinical decision support system utilizes advanced machine learning 
    algorithms to assess cardiovascular disease risk based on comprehensive 
    patient health metrics and lifestyle factors.
    """)
    
    st.markdown("---")
    st.markdown("### 🔬 Model Information")
    st.markdown("""
    - **Training Dataset:** 7,000 patient records
    - **Features Analyzed:** 14 clinical indicators
    - **Purpose:** Risk stratification & screening
    """)
    
    st.markdown("---")
    st.markdown("### 📋 Assessment Process")
    st.markdown("""
    1. **Input Data:** Complete all patient information fields
    2. **Validation:** System validates data integrity
    3. **Analysis:** ML model processes health indicators
    4. **Results:** Receive risk assessment with recommendations
    """)
    
    st.markdown("---")
    st.markdown("### ⚕️ Important Notice")
    st.warning("""
    This tool is designed for educational and screening purposes only. 
    It does not replace professional medical diagnosis or clinical judgment.
    """)

# Header section
st.title("🫀 Cardiovascular Disease Risk Assessment System")
st.markdown("---")

# Introduction
st.markdown("""
<div class="info-box">
<h3>Welcome to the Professional Heart Health Assessment Platform</h3>
<p>This evidence-based risk assessment tool employs machine learning methodology to evaluate 
cardiovascular disease probability through comprehensive analysis of clinical parameters, 
lifestyle factors, and patient demographics. The system provides data-driven insights to 
support early detection and preventive care strategies.</p>
</div>
""", unsafe_allow_html=True)

st.info("📌 **Note:** All information provided is confidential and used solely for risk calculation purposes.")


# Input form section
st.markdown("---")
st.markdown("## 📝 Patient Information & Clinical Data Entry")
st.markdown("Please provide accurate information for all fields to ensure optimal assessment accuracy.")

# Create tabs for organized input
tab1, tab2, tab3, tab4 = st.tabs(["👤 Demographics & Vitals", "🧬 Medical History", "💊 Lifestyle Factors", "🔬 Laboratory Values"])

# Tab 1: Demographics
with tab1:
    st.markdown("### Basic Patient Information")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age (Years)", min_value=1, max_value=120)
        gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Female" if x == 1 else "Male")
        bmi = st.number_input("BMI", min_value=3.47, max_value=300.5)
    
    with col2: 
        height = st.number_input("Height (cm)", min_value=50, max_value=250)
        weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0)
     
# Tab 2: Medical History
with tab2:
    st.markdown("### Medical History & Risk Factors")
    col1, col2 = st.columns(2)
    
    with col1:
        ap_hi = st.number_input("Systolic Blood Pressure (ap_hi)", min_value=50, max_value=250)  
    
    with col2:
        ap_lo = st.number_input("Diastolic Blood Pressure (ap_lo)", min_value=30, max_value=200)

# Tab 3: Lifestyle
with tab3:
    st.markdown("### Lifestyle & Behavioral Factors")
    col1, col2 = st.columns(2)
    
    with col1:
        smoke = st.selectbox("Smoking Status", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        alco = st.selectbox("Alcohol Intake", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    
    with col2:
        active = st.selectbox("Physical Activity", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        substance = st.number_input("Substance Used", min_value=10.0, max_value=300.0)

# Tab 4: Laboratory Values
with tab4:
    st.markdown("### Laboratory Values & Calculated Metrics")
    col1, col2 = st.columns(2)
    
    with col1:
        cholesterol = st.slider("Cholesterol Level", 1, 3, 1)
    
    with col2:
        gluc = st.slider("Glucose Level", 1, 3, 1)

# Automatically calculated BMI
#bmi = round(weight / ((height / 100) ** 2), 2) if height > 0 else 0
#st.write(f'**Calculated BMI:** {bmi}')


# Prepare input data 
features = pd.DataFrame([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi, substance ]], 
                        columns=['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'bmi',  
                                 'substance used'])

# Prediction
if st.button('Predict Heart Disease Risk'):
    try:
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        
       
        st.markdown("## 📊 Assessment Results")


        if prediction == 1:
            st.markdown("""
            <div style='background-color: #fef2f2; padding: 30px; border-radius: 10px; border-left: 6px solid #dc2626;'>
            <h2 style='color: #dc2626; margin-top: 0;'>⚠️ HIGH CARDIOVASCULAR RISK DETECTED</h2>
            <p style='font-size: 16px; color: #7f1d1d;'> The risk assessment model has identified a <strong>high probability</strong> of        
            cardiovascular  
            disease based on the provided clinical and lifestyle data. <strong>Immediate medical consultation is strongly recommended.</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🏥 Recommended Clinical Actions")            
            col1, col2 = st.columns(2)             
            
            with col1:
                st.markdown("""
                **Immediate Steps:**
                - 🩺 Schedule comprehensive cardiac evaluation
                - 📋 Complete full lipid panel and cardiac biomarkers
                - 💊 Review and optimize medication regimen
                - 📊 Baseline ECG and stress testing
                - 🔬 Consider advanced cardiac imaging if indicated
                """)
            
            with col2:
                st.markdown("""
                **Lifestyle Interventions:**
                - 🥗 Adopt DASH or Mediterranean diet
                - 🚭 Immediate smoking cessation support
                - 🏃‍♂️ Supervised cardiac rehabilitation program
                - 😌 Stress management and mental health support
                - 💤 Sleep hygiene optimization
                """)      
            
            st.markdown("### 📈 Monitoring Protocol")
            st.markdown("""
            - **Follow-up Frequency:** Every 3-6 months or as directed by cardiologist
            - **Key Metrics to Track:** Blood pressure, cholesterol, weight, physical activity
            - **Emergency Signs:** Chest pain, shortness of breath, palpitations, unusual fatigue
            """)
        
        else:
            st.markdown("""
            <div style='background-color: #f0fdf4; padding: 30px; border-radius: 10px; border-left: 6px solid #16a34a;'>
            <h2 style='color: #16a34a; margin-top: 0;'>✅ LOW CARDIOVASCULAR RISK</h2>
            <p style='font-size: 16px; color: #14532d;'> The assessment indicates a <strong>low probability</strong> of cardiovascular disease  
            based on current health metrics. Continue maintaining healthy lifestyle practices and regular health monitoring.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 💚 Preventive Health Maintenance")       
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **Continue Current Practices:**
                - ✅ Maintain balanced, nutrient-rich diet
                - ✅ Regular cardiovascular exercise routine
                - ✅ Consistent sleep schedule (7-9 hours)
                - ✅ Stress management techniques
                - ✅ Avoid tobacco and limit alcohol
                """)
            
            with col2:
                st.markdown("""
                **Routine Monitoring:**
                - 📅 Annual health check-ups
                - 🩺 Blood pressure monitoring
                - 📊 Lipid panel every 2-5 years
                - ⚖️ Maintain healthy weight
                - 🏃 Stay physically active
                """)
            
            st.markdown("### 🎯 Optimization Opportunities")
            st.info("""
            Even with low risk, there's always room for improvement. Consider:
            - Increasing physical activity if below recommended levels
            - Further dietary improvements (more vegetables, whole grains)
            - Enhanced stress reduction techniques (meditation, yoga)
            - Building strong social connections for mental health
            """)
    
    except Exception as e:
        st.error(f"❌ Error during risk assessment: {str(e)}")
        st.info("Please verify all input fields are completed correctly and try again.")

# General recommendations
st.markdown("---")
st.markdown("### 📚 Evidence-Based Resources")
st.markdown("""
- **American Heart Association:** Heart-healthy living guidelines
- **CDC Heart Disease Prevention:** www.cdc.gov/heartdisease
- **National Heart, Lung, and Blood Institute:** Educational materials
- **Local Cardiac Rehabilitation Programs:** Contact your healthcare provider
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='background-color: #eff6ff; padding: 25px; border-radius: 8px; margin-top: 30px;'>
    <h3 style='color: #1e40af; margin-top: 0;'>⚕️ Medical Disclaimer & Important Information</h3>
    <p style='color: #1e3a8a; line-height: 1.6;'>
    <strong>This risk assessment tool is intended for educational and screening purposes only.</strong> 
    However, this system does <strong>NOT</strong> constitute medical diagnosis, treatment advice, 
    or a substitute for professional healthcare consultation.
    </p>
    <p style='color: #1e3a8a; line-height: 1.6;'>
    <strong>Action Required:</strong> If you have concerns about your cardiovascular health, experience 
    symptoms, or receive a high-risk assessment, please consult with a licensed healthcare provider immediately. 
    In case of emergency (chest pain, difficulty breathing), call emergency services (911 in US).
    </p>
    <hr style='border: 1px solid #93c5fd; margin: 15px 0;'>
    <p style='color: #1e40af; text-align: center; margin-bottom: 0; font-size: 14px;'>
    © 2025 Heart Disease Risk Assessment System | For Healthcare Professional & Educational Use
    </p>
</div>
""", unsafe_allow_html=True)
