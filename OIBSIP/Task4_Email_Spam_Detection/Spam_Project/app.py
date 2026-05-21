#import libraries
import streamlit as st #for interactive dashboard
import pandas as pd #for file read and data manipulation
import numpy as np #for numeric calculations
import plotly.express as px #for interactive data visualization
import joblib #to load model

#page settings
st.set_page_config(
    page_title='Email Spam Detection Dashboard',
    page_icon='📧',
    layout='wide'
)

#load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

#header

#title
st.title("📧 Email Spam Detection Dashboard")

#description
st.markdown("""
Detect whether a message is Spam or Not Spam using Machine Learning.
""")

#sidebar

#header
st.sidebar.header("About Project")

st.sidebar.info("""
This dashboard uses NLP and Machine Learning
to classify messages as Spam or Not Spam.
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Examples")
st.sidebar.write("Spam: Congratulations! You won ₹50,000. Click now.")
st.sidebar.write("Normal: Hey, let's meet tomorrow at 4 PM.")

st.markdown("---")

#sample KPI section
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Type", "ML Classifier")

with col2:
    st.metric("Input Type", "Text")

with col3:
    st.metric("Output", "Spam/Not Spam")

st.markdown("---")

#prediction section
st.subheader("🔮 Message Prediction")

message = st.text_area(
    "Enter Message",
    height = 150,
    placeholder = "Type your email/message here..."
)

if st.button("Detect Message"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed = vectorizer.transform([message])
        prediction = model.predict(transformed)[0]

        if prediction == 1:
            st.error("🚫 Spam Message Detected")
        else:
            st.success("✅ Not Spam Message")

st.markdown("---")

#insights
st.subheader("Key Insights")
st.markdown("""
- Spam messages often contain prizes, rewards and urgency.
- Words like "free", "winner", "click now" are common.
- NLP converts text into numerical features.
- Machine Learning learns patterns from past messages.
- Detection improves email security.
""")

st.markdown("---")

#footer
st.markdown('<h3 style = "text-align : center; color : #ffb6c1;">🌸 Made By Panthini Patel</h3>', unsafe_allow_html = True)
st.markdown('<p style = "text-align : center; font-size : 20px;">🚀 Made Using Streamlit</p>', unsafe_allow_html = True) 