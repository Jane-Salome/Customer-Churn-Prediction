# Customer Churn Prediction System 📊

**Live Demo** → [Click here to view the app](https://customer-churn-prediction-jz7ygrxvyzqjc86aqw9uyg.streamlit.app/)

A machine learning web application that predicts the likelihood of a customer churning based on their profile, subscription details, and usage patterns — helping businesses identify high-risk customers and improve retention strategies.

---

## Features

- **Churn Probability Score** — Predicts churn likelihood as a percentage (0–100%)
- **Risk Classification** — Categorizes customers into Low, Medium, or High risk
- **Interactive Input Form** — Enter customer details through a clean Streamlit UI
- **Real-time Prediction** — Instant results powered by a pre-trained Logistic Regression model
- **Visual Progress Bar** — Shows churn probability visually for quick interpretation
- **Detailed Customer Profiling** — Accepts age, tenure, usage frequency, support calls, payment delay, subscription type, contract length, and total spend

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Frontend | Streamlit |
| ML Model | Logistic Regression (scikit-learn) |
| Data Handling | pandas |
| Model Serialization | joblib (.pkl files) |
| Dataset | Customer Churn Dataset (training) |

---

## How It Works

1. **Input** — User fills in customer details (demographics, subscription info, usage behavior)
2. **Encoding** — Categorical variables (Gender, Subscription Type, Contract Length) are encoded to match training data
3. **Scaling** — Input is scaled using the pre-fitted StandardScaler
4. **Prediction** — Logistic Regression model predicts churn class and probability
5. **Output** — Displays churn probability %, a visual progress bar, and a risk label:
   - 🟢 Low Risk — below 40%
   - 🟡 Medium Risk — 40% to 70%
   - 🔴 High Risk — above 70%

---

## Project Structure

```
├── app.py                                      # Main Streamlit application
├── logistic_model.pkl                          # Trained Logistic Regression model
├── scaler.pkl                                  # Fitted StandardScaler
├── features.pkl                                # Feature column names
├── customer_churn_dataset-training-master.csv  # Training dataset
└── requirements.txt                            # Project dependencies
```

---

## Getting Started

### Prerequisites
Python 3.8+

### Installation

```bash
# Clone the repository
git clone https://github.com/Jane-Salome/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## Input Features

| Feature | Description |
|---|---|
| Age | Customer age |
| Gender | Male / Female |
| Tenure | Months as a customer |
| Usage Frequency | Number of interactions per month |
| Support Calls | Number of support calls made |
| Payment Delay | Days of payment delay |
| Subscription Type | Basic / Standard / Premium |
| Contract Length | Monthly / Quarterly / Yearly |
| Total Spend | Total amount spent ($) |
| Last Interaction | Days since last interaction |

---

## Author

**Jane Salome D**  
B.Tech Information Technology — Sri Sairam Engineering College  
[LinkedIn](https://www.linkedin.com/in/jane-salome-d-a47a91295) | [GitHub](https://github.com/Jane-Salome)
