# FIR / Complaint Classification and Priority System

An AI-powered complaint management system that uses Natural Language Processing (NLP) and Machine Learning to automatically classify complaint text, analyze sentiment, and assign priority levels for faster and smarter resolution.

---

## 📌 Project Overview

Manual complaint handling is time-consuming and can delay urgent cases. This project automates the complaint analysis process by reading complaint text and generating structured outputs that help organizations respond efficiently.

The system predicts:

- Complaint Category  
- Sentiment  
- Priority Level  

This solution can be applied in:

- Police Complaint Portals  
- Government Grievance Systems  
- Banking Complaint Platforms  
- Customer Support Services  

---

## ✨ Key Features

- Automated Complaint Classification  
- Sentiment Analysis  
- Priority Prediction  
- Real-Time Prediction Interface using Streamlit  
- Fast and Scalable Processing  
- Clean and User-Friendly UI  

---

## 🛠 Technology Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Natural Language Processing (NLP)  
- TF-IDF Vectorization  
- Logistic Regression  
- Streamlit  

---

## 📂 Dataset Information

The project uses a complaint dataset containing real complaint narratives across multiple categories, including:

- credit_card  
- credit_reporting  
- debt_collection  
- mortgages_and_loans  
- retail_banking  

The text data was cleaned, preprocessed, and transformed into numerical features before model training.

---

## ⚙️ Machine Learning Workflow

1. Data Collection  
2. Text Cleaning and Preprocessing  
3. Label Encoding  
4. TF-IDF Vectorization  
5. Train-Test Split  
6. Logistic Regression Model Training  
7. Model Evaluation  
8. Deployment using Streamlit  

---

## 📊 Model Output

For each complaint entered by the user, the system predicts:

- Complaint Category  
- Sentiment (Positive / Neutral / Negative)  
- Priority Level (High / Medium / Low)

---

## 🖥️ Application Screenshots

### Home Page

![Home Page](Streamlit%20UI/Home%20Page.png)

### Prediction Result

![Prediction Result](Streamlit%20UI/Prediction%20Result%20Page.png)

---
---

## 👨‍💻 Author

**Maaz Patel**  
BSc Information Technology Graduate  
Aspiring Data Analyst | Machine Learning Enthusiast

- GitHub: https://github.com/PatelMaaz2004
- LinkedIn: https://www.linkedin.com/in/patel-maaz-0410mp

---

## 📁 Repository Structure

```text
FIR-Complaint-Classification-and-Priority-System/
│── Complaint_Classification_Model.ipynb
│── README.md
│── Complaint Classification and Priority System.pptx
│── FIR & Complaint Classification and Priority System.pdf
│
├── Deployment/
│   ├── app.py
│   ├── complaint_model.pkl
│   ├── label_encoder.pkl
│   └── tfidf_vectorizer.pkl
│
├── Streamlit UI/
│   ├── Home Page.png
│   └── Prediction Result Page.png
