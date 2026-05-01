import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    /* Neon gradient background */
    background: linear-gradient(135deg, #ff00ff, #00ffff, #ffea00, #ff0080);
    background-size: 400% 400%;
    animation: gradientAnimation 15s ease infinite;
    color: #ffffff;
}

/* Text styling */
h1, h2, h3, h4, h5, h6, label, p, div, span {
    color: #ffffff !important;
    font-weight: 600;
}

/* Gradient animation */
@keyframes gradientAnimation {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# CUSTOM CSS (FOR PROFESSIONAL LOOK)
# ---------------------------------------------------
st.markdown("""
<style>
/* Make all main text dark */
h1, h2, h3, h4, h5, h6, label, p, div, span {
    color: #1a1a1a !important;  /* Dark black for readability */
    font-weight: 600;
}

/* Input labels */
.css-1cpxqw2 label {
    color: #1a1a1a !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background-color: #2563eb;  /* Blue button */
    color: white;
    font-size: 18px;
    border-radius: 10px;
}
.stButton > button:hover {
    background-color: #1e40af;
}

/* Card background */
.card {
    background-color: #f5f5f5;  /* Light grey card */
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: #1a1a1a;  /* Dark text inside card */
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
input, .st-bx {
    color: #1a1a1a !important;  /* Dark text inside inputs */
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------
try:
    features = joblib.load("features.pkl")
    model = joblib.load("logistic_model.pkl")
    scaler = joblib.load("scaler.pkl")
except:
    st.error("❌ Model files not found. Keep all .pkl files in the same folder.")
    st.stop()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("📘 App Instructions")
st.sidebar.write("""
Fill in customer details and click **Predict Churn**
to view churn probability and risk level.
""")

st.sidebar.markdown("## 📊 About Project")
st.sidebar.write("""
**Model:** Logistic Regression  
**Technology:** Python, Scikit-Learn, Streamlit  
**Purpose:** Customer churn prediction
""")

# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------
st.title("🔮 Customer Churn Prediction System")
st.write("Provide customer information below to estimate churn risk.")

# ---------------------------------------------------
# CUSTOMER INFORMATION
# ---------------------------------------------------
st.header("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    customer_id = st.number_input("Customer ID", min_value=1)
    age = st.number_input("Age", min_value=18, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female"])

with col2:
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=120)
    usage = st.number_input("Usage Frequency (per month)", min_value=0, max_value=200)
    last_interaction = st.number_input("Days Since Last Interaction", min_value=0, max_value=365)

# ---------------------------------------------------
# SUBSCRIPTION DETAILS
# ---------------------------------------------------
st.header("📄 Subscription Details")

col3, col4 = st.columns(2)

with col3:
    subscription = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
    contract = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Yearly"])

with col4:
    support_calls = st.number_input("Support Calls", min_value=0, max_value=50)
    payment_delay = st.number_input("Payment Delay (days)", min_value=0, max_value=365)
    total_spend = st.number_input("Total Spend ($)", min_value=0.0, max_value=100000.0)

# ---------------------------------------------------
# ENCODING (MATCH TRAINING)
# ---------------------------------------------------
gender_map = {"Female": 0, "Male": 1}
subscription_map = {"Basic": 0, "Premium": 1, "Standard": 2}
contract_map = {"Monthly": 0, "Quarterly": 1, "Yearly": 2}

input_dict = {
    "CustomerID": customer_id,
    "Age": age,
    "Gender": gender_map[gender],
    "Tenure": tenure,
    "Usage Frequency": usage,
    "Support Calls": support_calls,
    "Payment Delay": payment_delay,
    "Subscription Type": subscription_map[subscription],
    "Contract Length": contract_map[contract],
    "Total Spend": total_spend,
    "Last Interaction": last_interaction
}

input_data = pd.DataFrame(
    [[input_dict[col] for col in features]],
    columns=features
)

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------
if st.button("Predict Churn"):

    scaled_input = scaler.transform(input_data)

    pred_class = model.predict(scaled_input)[0]
    pred_prob = model.predict_proba(scaled_input)[0][1]

    prob_percent = round(pred_prob * 100, 2)

    if prob_percent < 40:
        risk = "🟢 Low Risk"
        color = "green"
    elif prob_percent < 70:
        risk = "🟡 Medium Risk"
        color = "orange"
    else:
        risk = "🔴 High Risk"
        color = "red"

    # ---------------------------------------------------
    # RESULTS
    # ---------------------------------------------------
    st.subheader("📊 Prediction Results")

    st.metric("Churn Probability", f"{prob_percent}%")
    st.progress(int(prob_percent))

    st.markdown(f"""
    <div class="card">
        <h2 style="color:{color};">{risk}</h2>
    </div>
    """, unsafe_allow_html=True)

    if pred_class == 1:
        st.error("⚠ The customer is **LIKELY to churn**.")
    else:
        st.success("✅ The customer is **NOT likely to churn**.")