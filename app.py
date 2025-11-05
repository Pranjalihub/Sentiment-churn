import streamlit as st
import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not already present
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()
# Load model and encoders
model = pickle.load(open("churn_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

st.title("📊 Customer Sentiment & Churn Prediction App")

# --- Sentiment Analysis ---
st.header("📝 Sentiment Analysis")
feedback = st.text_area("Enter customer feedback here:")

def get_sentiment(text):
    score = sid.polarity_scores(text)
    compound = score['compound']
    if compound > 0.05:
        return "positive"
    elif compound < -0.05:
        return "negative"
    else:
        return "neutral"

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




