# 🚫📧 Email Spam Detection using Machine Learning

## 📌 Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) to classify emails/messages as Spam or Ham (Not Spam).

The model learns patterns from text messages and predicts whether a new message is spam or genuine.

---

## 📊 Dataset Features

- v1 → Label (Spam or Ham)
- v2 → Message Text

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- NLTK
- Streamlit
- Joblib

---

## 📈 Key Insights

- Most messages in the dataset are non-spam.
- Spam messages usually contain promotional words.
- Spam texts are generally longer than ham messages.
- Words like "Free", "Win", and "Prize" appear frequently in spam messages.

---

## 🤖 Machine Learning Model

### Model Used:
- Multinomial Naive Bayes

### Techniques Used:
- Text Cleaning
- Tokenization
- Stopword Removal
- TF-IDF Vectorization

---

## 🚀 Streamlit Dashboard

The interactive dashboard allows users to:
- Enter custom messages
- Detect spam instantly
- View prediction results in real time

---

## 📂 Project Structure

```text
Task4_Email_Spam_Detection/
│
├── Spam_Project/
│     ├── app.py
│     ├── spam.csv
│     ├── spam_model.pkl
│     ├── vectorizer.pkl
│     ├── Message_Length_Comparison.png
│     └── Spam_VS_Ham.png
│
├── Task4/
│     ├── PanthiniPatel_Task4.ipynb
│     ├── spam.csv
│     ├── spam_model.pkl
│     ├── vectorizer.pkl
│     ├── Message_Length_Comparison.png
│     └── Spam_VS_Ham.png
│
└── README.md
```

---

# ▶️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/panthinipatel5/OIBSIP.git
```

---

## 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---


## 💾 Model Saving

```python
joblib.dump(model, "spam_model.pkl")
joblib.dump(tfidf, "vectorizer.pkl")
```

---

## 📌 Future Improvements

- Deep Learning Models
- Better UI Design
- Live Email Integration
- Deployment on Streamlit Cloud

---

## 📜 License

This project is open-source and free to use.

---

# 👨‍💻 Author

Panthini Patel
