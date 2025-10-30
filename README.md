# Sentiment-churn
This project combines Sentiment Analysis and Customer Churn Prediction to help businesses understand customer behavior and take proactive actions to reduce churn. It uses Machine Learning and Natural Language Processing to analyze customer feedback and predict whether a customer is likely to leave based on both text sentiment and customer data.

Key Features
🧠 Sentiment Analysis:
Uses NLP techniques (TF-IDF, Bag of Words, or embeddings) to classify customer feedback as positive, negative, or neutral.
📉 Churn Prediction Model:
Predicts the probability of customer churn using classification algorithms such as Logistic Regression, Random Forest, or XGBoost.
📊 Data Preprocessing:
Handles missing values, encodes categorical variables, and scales numerical data for model training.
💾 Model Saving & Deployment:
Trained models are saved using Pickle and loaded into a Streamlit web app for live predictions.
🧩 Interactive Web App:
Built with Streamlit for user-friendly input and real-time prediction results.

🧰 Tech Stack
Languages: Python
Libraries: pandas, numpy, scikit-learn, nltk / textblob, streamlit, pickle
Tools: Jupyter Notebook, Google Colab
Visualization: matplotlib, seaborn

🧪 How It Works
Data Collection: Import customer data and text reviews.
Data Cleaning: Handle missing values, perform text preprocessing (tokenization, stopword removal, lemmatization).
Feature Engineering: Create sentiment scores and merge them with customer demographic or behavioral data.
Model Training: Train separate models for sentiment classification and churn prediction.
Model Evaluation: Evaluate performance using accuracy, F1-score, precision, recall, and ROC-AUC.
Deployment: Load trained models into a Streamlit app for live testing and visualization.
Deployment: Load trained models into a Streamlit app for live testing and visualization.
