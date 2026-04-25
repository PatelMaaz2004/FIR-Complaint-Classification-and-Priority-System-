
import streamlit as st
import joblib
from textblob import TextBlob

# Load saved files
model = joblib.load("complaint_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
le = joblib.load("label_encoder.pkl")

# Title
st.title("FIR / Complaint Classification System")
st.subheader("AI-Based Complaint Category, Sentiment & Priority Predictor")

# Input box
user_input = st.text_area("Enter Complaint Text")

# Priority function
def get_priority(text, sentiment):
    text = text.lower()

    urgent_words = ['fraud', 'stolen', 'harassment', 'threat', 'scam', 'urgent']

    if any(word in text for word in urgent_words):
        return "High"
    elif sentiment < 0:
        return "Medium"
    else:
        return "Low"

# Predict button
if st.button("Predict"):

    if user_input.strip() != "":

        # Category Prediction
        vector = tfidf.transform([user_input])
        pred = model.predict(vector)
        category = le.inverse_transform(pred)[0]

        # Sentiment
        sentiment_score = TextBlob(user_input).sentiment.polarity

        if sentiment_score < 0:
            sentiment = "Negative"
        elif sentiment_score == 0:
            sentiment = "Neutral"
        else:
            sentiment = "Positive"

        # Priority
        priority = get_priority(user_input, sentiment_score)

        # Output
        st.success("Prediction Complete")

        st.write("### Complaint Category:", category)
        st.write("### Sentiment:", sentiment)
        st.write("### Priority Level:", priority)

    else:
        st.warning("Please enter complaint text.")
