import streamlit as st
import pickle
# Load model and encoders
model = pickle.load(open("churn_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

st.title("📊 Customer Sentiment & Churn Prediction App")

# --- Sentiment Analysis ---
st.header("📝 Sentiment Analysis")
feedback = st.text_area("Enter customer feedback here:")

if st.button("Analyze Sentiment"):
    polarity = TextBlob(feedback).sentiment.polarity
    if polarity > 0:
        st.success("Sentiment: Positive 😀")
    elif polarity < 0:
        st.error("Sentiment: Negative 😞")
    else:
        st.info("Sentiment: Neutral 😐")

# --- Churn Prediction ---
st.header("🔮 Churn Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
monthly = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)

if st.button("Predict Churn"):
    gender_encoded = encoders["gender"].transform([gender])[0]
    input_data = [[gender_encoded, tenure, monthly]]
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.warning("⚠️ This customer is likely to churn.")
    else:

        st.success("✅ This customer is likely to stay.")


