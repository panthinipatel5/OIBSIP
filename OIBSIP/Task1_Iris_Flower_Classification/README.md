# 🌸 Iris Flower Classification Dashboard

## Machine Learning Based Flower Species Prediction System

An interactive Machine Learning project built using **Python**, **Scikit-learn**, and **Streamlit** that predicts the species of an Iris flower based on flower measurements.

The dashboard combines **Exploratory Data Analysis (EDA)**, interactive visualizations, and a trained Machine Learning model to provide accurate real-time predictions.

---

# 🏆 Oasis Infobyte Internship Task

This project was completed as part of the **Oasis Infobyte Data Science Internship Program (OIBSIP)**.

### Task Details

| Field              | Details                                         |
| ------------------ | ----------------------------------------------- |
| Internship Program | Oasis Infobyte Data Science Internship (OIBSIP) |
| Task Number        | Task 1                                          |
| Task Name          | Iris Flower Classification                      |
| Domain             | Machine Learning Classification                 |
| Model Type         | Supervised Learning                             |
| Deployment         | Streamlit Dashboard                             |

---

# 🎯 Project Objective

The objective of this project is to build a Machine Learning classification system capable of accurately identifying Iris flower species based on flower measurements.

This project demonstrates the complete Data Science workflow including:

* Data Collection
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Machine Learning Model Training
* Model Evaluation
* Interactive Dashboard Development

The final solution provides real-time flower species prediction through an easy-to-use Streamlit interface.

---

# 🌍 Problem Statement

Identifying flower species manually can be time-consuming and requires botanical expertise.

This project automates the classification process by leveraging Machine Learning algorithms to predict flower species based on measurable characteristics such as:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The system provides fast, accurate, and consistent predictions that can assist students, researchers, and data science learners.

---

# 🚀 Project Features

* 🌸 Iris flower species prediction
* 📊 Interactive Streamlit dashboard
* 📈 Exploratory Data Analysis (EDA)
* 🔥 Correlation heatmap visualization
* 🌿 Pairplots and scatterplots
* 📉 Feature comparison charts
* 🤖 Random Forest Classification model
* 📋 Dataset preview and statistics
* 🎯 Real-time prediction system

---

# 🌼 Iris Species Classification

The model predicts the following flower species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

# 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn
* Joblib

---

# 📂 Dataset Information

The Iris dataset contains flower measurements used for classification.

## 📌 Dataset Features

| Feature      | Description     |
| ------------ | --------------- |
| Sepal Length | Length of sepal |
| Sepal Width  | Width of sepal  |
| Petal Length | Length of petal |
| Petal Width  | Width of petal  |

### Dataset Purpose

The dataset is widely used in Machine Learning for classification tasks and serves as a benchmark dataset for supervised learning algorithms.

---

# 📊 Exploratory Data Analysis (EDA)

The project includes detailed data analysis and visualization such as:

* Dataset overview
* Statistical summary
* Pairplot analysis
* Scatterplot visualization
* Correlation heatmap
* Species distribution analysis

### EDA Objectives

* Understand feature distributions
* Identify correlations between variables
* Analyze species separation patterns
* Discover important classification features

---

# 📈 Key Insights

* Petal length and petal width are highly important for classification.
* Iris-setosa is easily separable from other species.
* Some overlap exists between versicolor and virginica species.
* Strong correlation exists between petal features.

---

# 🤖 Machine Learning Model

## ✅ Model Used

* Random Forest Classifier

### Why Random Forest?

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

---

## ⚙️ ML Workflow

```text
1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Real-Time Prediction
```

---

# 📉 Model Performance

The Random Forest model provides high accuracy for flower species prediction using flower measurements.

### 📌 Evaluation Metrics

* Accuracy Score
* Confusion Matrix
* Classification Report

### Results

The model successfully classifies:

✅ Iris-setosa

✅ Iris-versicolor

✅ Iris-virginica

The trained model demonstrated reliable performance across all three flower categories.

---

# 🖥️ Interactive Dashboard

The Streamlit dashboard allows users to:

* Enter flower measurements
* Predict Iris species instantly
* Explore dataset visualizations
* Analyze feature relationships
* View prediction outputs interactively

### Dashboard Capabilities

✔ Real-Time Prediction

✔ Interactive User Inputs

✔ Dynamic Visualizations

✔ Dataset Exploration

✔ Model Demonstration

---

# 📸 Project Screenshots

The repository contains screenshots demonstrating:

* Dataset Preview
* Statistical Analysis
* Pairplot Visualization
* Correlation Heatmap
* Feature Relationships
* Model Predictions
* Streamlit Dashboard Interface

Example folder structure:

```text
screenshots/
├── Correlation Heatmap.png
├── Prediction_Output.png
├── Dataset Preview.png
├── Features Relationship.png
├── PetalLength_VS_PetalWidth.png
├── SepalLength_Distribution.png
├── Species Distribution.png
├── Statistical Summary.png
└── Dashboard.png
```

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
├── screenshots/
│     ├── Correlation Heatmap.png
│     ├── Prediction_Output.png
│     ├── Dataset Preview.png
│     ├── Features Relationship.png
│     ├── PetalLength_VS_PetalWidth.png
│     ├── SepalLength_Distribution.png
│     ├── Species Distribution.png
│     ├── Statistical Summary.png
│     └── Dashboard.png
│
└── README.md
```

---

# ▶️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/panthinipatel5/OIBSIP.git
```

## 2️⃣ Navigate to Project Folder

```bash
cd Task1_Iris_Flower_Classification
```

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

# 💾 Model Saving

```python
joblib.dump(model, "iris_model.pkl")
```

The trained model is serialized using Joblib, allowing it to be loaded instantly for future predictions without retraining.

---

# 🎓 Skills Learned

During the development of this project, the following skills were strengthened:

✔ Data Cleaning and Preparation

✔ Exploratory Data Analysis

✔ Feature Correlation Analysis

✔ Machine Learning Classification

✔ Model Evaluation Techniques

✔ Data Visualization

✔ Streamlit Dashboard Development

✔ Model Serialization using Joblib

✔ End-to-End Project Documentation

---

# 📌 Conclusion

This project successfully demonstrates how Machine Learning can be applied to solve a multi-class classification problem.

By combining data analysis, visualization, model training, and dashboard development, the system provides an effective solution for Iris flower species prediction.

The project highlights practical applications of Data Science concepts and serves as a strong foundation for more advanced classification systems.

---

# 🌟 Future Improvements

* Deep Learning based classification
* Better UI/UX design
* Deployment on Streamlit Cloud
* Additional flower datasets
* Advanced visualization dashboard
* Mobile-friendly dashboard interface
* Model comparison with other classification algorithms

---

# 📜 License

This project is open-source and available for educational and learning purposes.

---

# 👨‍💻 Author

### Panthini Patel

Data Science • Machine Learning • Analytics

Developed as part of the **Oasis Infobyte Data Science Internship Program (OIBSIP)**.

⭐ If you found this project useful, consider giving it a star.
