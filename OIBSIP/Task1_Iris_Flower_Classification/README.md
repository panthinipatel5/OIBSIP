# 🌸 Iris Flower Classification Dashboard  
## Machine Learning Based Flower Species Prediction System

An interactive Machine Learning project built using **Python**, **Scikit-learn**, and **Streamlit** that predicts the species of an Iris flower based on flower measurements.  

The dashboard combines **Exploratory Data Analysis (EDA)**, interactive visualizations, and a trained Machine Learning model to provide accurate real-time predictions.

---

# 🚀 Project Features

- 🌸 Iris flower species prediction
- 📊 Interactive Streamlit dashboard
- 📈 Exploratory Data Analysis (EDA)
- 🔥 Correlation heatmap visualization
- 🌿 Pairplots and scatterplots
- 📉 Feature comparison charts
- 🤖 Random Forest Classification model
- 📋 Dataset preview and statistics
- 🎯 Real-time prediction system

---

# 🌼 Iris Species Classification

The model predicts the following flower species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

---

# 🧠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib

---

# 📂 Dataset Information

The Iris dataset contains flower measurements used for classification.

## 📌 Dataset Features

| Feature | Description |
|---|---|
| Sepal Length | Length of sepal |
| Sepal Width | Width of sepal |
| Petal Length | Length of petal |
| Petal Width | Width of petal |

---

# 📊 Exploratory Data Analysis (EDA)

The project includes detailed data analysis and visualization such as:

- Dataset overview
- Statistical summary
- Pairplot analysis
- Scatterplot visualization
- Correlation heatmap
- Species distribution analysis

---

# 📈 Key Insights

- Petal length and petal width are highly important for classification.
- Iris-setosa is easily separable from other species.
- Some overlap exists between versicolor and virginica species.
- Strong correlation exists between petal features.

---

# 🤖 Machine Learning Model

## ✅ Model Used
- Random Forest Classifier

## ⚙️ ML Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Real-Time Prediction

---

# 📉 Model Performance

The Random Forest model provides high accuracy for flower species prediction using flower measurements.

### 📌 Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report

---

# 🖥️ Interactive Dashboard

The Streamlit dashboard allows users to:

- Enter flower measurements
- Predict Iris species instantly
- Explore dataset visualizations
- Analyze feature relationships
- View prediction outputs interactively

---

# 📂 Project Structure

```text
Task1_Iris_Flower_Classification/
│
├── Iris_Project/
│     ├── Iris.csv
│     ├── app.py
│     ├── iris_model.pkl
│     └── pairplot.png
│
├── Task1/
│     ├── Iris.csv
│     ├── PanthiniPatel_Task1.ipynb
│     ├── iris_model.pkl
│     └── pairplot.png
│
└── README.md
```

---


# ▶️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/panthinipatel5/Iris-Flower-Classification.git
```
---

## 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 💾 Model Saving

```python
joblib.dump(model, "iris_model.pkl")
```

---

# 🌟 Future Improvements

- Deep Learning based classification
- Better UI/UX design
- Deployment on Streamlit Cloud
- Additional flower datasets
- Advanced visualization dashboard

---

# 📜 License

This project is open-source and available for educational and learning purposes.

---

# 👨‍💻 Author

Panthini Patel
