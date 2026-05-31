# 🚗 Car Price Prediction using Machine Learning

## Intelligent Vehicle Price Estimation System

An interactive Machine Learning project built using **Python**, **Scikit-learn**, and **Streamlit** to predict the selling price of used cars based on various vehicle features.

The project combines **Exploratory Data Analysis (EDA)**, data visualization, predictive modeling, and an interactive dashboard to estimate car resale prices accurately.

---

# 🏆 Oasis Infobyte Internship Task

This project was completed as part of the **Oasis Infobyte Data Science Internship Program (OIBSIP)**.

### Task Details

| Field              | Details                                         |
| ------------------ | ----------------------------------------------- |
| Internship Program | Oasis Infobyte Data Science Internship (OIBSIP) |
| Task Number        | Task 3                                          |
| Task Name          | Car Price Prediction with Machine Learning      |
| Domain             | Machine Learning & Predictive Analytics         |
| Model Type         | Regression                                      |
| Deployment         | Streamlit Dashboard                             |

---

# 🎯 Project Objective

The objective of this project is to develop a Machine Learning model capable of accurately predicting the resale value of used cars based on their specifications and historical data.

The project demonstrates:

* Data Cleaning and Preparation
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Predictive Modeling
* Model Evaluation
* Interactive Dashboard Development

The final solution helps users estimate a car's selling price instantly through a user-friendly Streamlit application.

---

# 🌍 Problem Statement

Determining the fair selling price of a used car can be challenging due to multiple factors such as age, mileage, fuel type, ownership history, and market trends.

This project aims to automate the price estimation process using Machine Learning techniques that analyze historical vehicle data and predict an expected selling price.

The system can assist:

* Car Buyers
* Car Sellers
* Dealerships
* Market Analysts
* Data Science Learners

in making data-driven decisions.

---

# 🚀 Project Features

* 🚗 Used car price prediction system
* 📊 Interactive Streamlit dashboard
* 📈 Exploratory Data Analysis (EDA)
* 🔥 Correlation heatmap visualization
* 📉 Price distribution analysis
* 🤖 Machine Learning prediction model
* 📋 Dataset statistics and insights
* 🎯 Real-time car price prediction

---

# 📂 Dataset Information

The dataset contains information about different cars and their selling prices.

## 📌 Dataset Features

| Feature       | Description               |
| ------------- | ------------------------- |
| Car_Name      | Name of the car           |
| Year          | Manufacturing year        |
| Selling_Price | Selling price of the car  |
| Present_Price | Current showroom price    |
| Driven_kms    | Total kilometers driven   |
| Fuel_Type     | Petrol / Diesel / CNG     |
| Selling_type  | Dealer or Individual      |
| Transmission  | Manual or Automatic       |
| Owner         | Number of previous owners |

### Dataset Purpose

The dataset is used to analyze factors affecting used car prices and train a machine learning model capable of estimating resale values.

---

# 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib

---

# 📊 Exploratory Data Analysis (EDA)

The project performs detailed data analysis including:

* Data cleaning
* Missing value checking
* Statistical summary
* Correlation analysis
* Price distribution visualization
* Feature relationship analysis

### EDA Objectives

* Understand vehicle pricing patterns
* Identify key factors affecting resale value
* Discover relationships among vehicle features
* Analyze feature importance
* Improve prediction performance

---

# 📈 Key Insights

* Most cars are priced below ₹10 Lakhs.
* Present price has a strong impact on selling price.
* Newer cars generally have higher resale value.
* Cars driven more kilometers usually have lower prices.
* Diesel vehicles often show better resale value.
* Automatic transmission cars are slightly more expensive.

---

# 🤖 Machine Learning Model

## ✅ Model Used

* Linear Regression

### Why Linear Regression?

Linear Regression is an effective baseline algorithm for understanding the relationship between vehicle attributes and selling prices while providing interpretable predictions.

---

## ⚙️ ML Workflow

```text
1. Load Dataset
2. Data Cleaning
3. Feature Encoding
4. Exploratory Data Analysis
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Real-Time Prediction
```

---

# 📉 Model Evaluation Metrics

The model was evaluated using:

* R² Score
* Mean Absolute Error (MAE)

These metrics help assess prediction accuracy and model performance.

### Results

The trained model successfully learned pricing patterns from historical vehicle data and generated reliable resale value predictions based on user inputs.

---

# 🖥️ Interactive Streamlit Dashboard

The dashboard allows users to:

* Enter car details
* Select fuel type
* Select transmission type
* Provide ownership information
* Predict selling price instantly
* Explore prediction results interactively

### Dashboard Capabilities

✔ Real-Time Prediction

✔ Interactive User Inputs

✔ Dynamic Output Display

✔ Vehicle Information Analysis

✔ User-Friendly Interface

---

# 📊 Business Value

The solution can be useful for:

* Used Car Dealerships
* Individual Buyers
* Individual Sellers
* Automobile Market Analysts

The model helps estimate a reasonable market price and supports informed decision-making during vehicle transactions.

---

# 📸 Project Screenshots

The repository contains screenshots demonstrating:

* Dataset Preview
* Price Distribution Analysis
* Correlation Heatmap
* Feature Relationships
* Model Predictions
* Streamlit Dashboard Interface

Example folder structure:

```text
screenshots/
├── Dataset Preview.png
├── Statistical Summary.png
├── Dashboard.png
├── Selling Price Distribution.png
├── Transmission Analysis.png
├── Year Wise Trend Analysis.png
├── Correlation Heatmap.png
├── Prediction_Output.png
└── Fuel Type Analysis
```

---

# 📂 Project Structure

```text
Task3_Car_Price_Prediction/
│
├── CarPrice_Project/
│     ├── app.py
│     ├── car data.csv
│     ├── car_price_model.pkl
│     ├── Car_Selling_Price_Distribution.png
│     └── Feature_Correlation.png
│
├── Task3/
│     ├── PanthiniPatel_Task3.ipynb
│     ├── car data.csv
│     ├── car_price_model.pkl
│     ├── Car_Selling_Price_Distribution.png
│     └── Feature_Correlation.png
│
├── screenshots/
│     ├── Dataset Preview.png
│     ├── Statistical Summary.png
│     ├── Dashboard.png
│     ├── Selling Price Distribution.png
│     ├── Transmission Analysis.png
│     ├── Year Wise Trend Analysis.png
│     ├── Correlation Heatmap.png
│     ├── Prediction_Output.png
│     └── Fuel Type Analysis
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
cd Task3_Car_Price_Prediction
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

The trained model is saved using Joblib:

```python
joblib.dump(model, "car_price_model.pkl")
```

The saved model can be loaded later without retraining, enabling fast predictions and deployment.

---

# 🎓 Skills Learned

During the development of this project, the following skills were strengthened:

✔ Data Cleaning and Preprocessing

✔ Feature Engineering

✔ Exploratory Data Analysis

✔ Correlation Analysis

✔ Regression Modeling

✔ Machine Learning Evaluation

✔ Data Visualization

✔ Streamlit Dashboard Development

✔ Predictive Analytics

✔ End-to-End Project Documentation

---

# 📌 Conclusion

This project successfully demonstrates how Machine Learning can be applied to predict used car prices based on vehicle characteristics.

By combining data analysis, predictive modeling, and interactive dashboard development, the system provides a practical solution for estimating vehicle resale values.

The project highlights real-world applications of Data Science and showcases how historical data can be transformed into actionable business insights.

---

# 🌟 Future Improvements

* Random Forest Models
* XGBoost Regression
* Advanced Feature Engineering
* Better UI/UX Dashboard Design
* Real-Time Market Price Integration
* Deployment on Streamlit Cloud
* Advanced Data Visualizations
* Deep Learning-Based Price Prediction

---

# 📜 License

This project is open-source and available for educational and learning purposes.

---

# 👨‍💻 Author

### Panthini Patel

Data Science • Machine Learning • Analytics

Developed as part of the **Oasis Infobyte Data Science Internship Program (OIBSIP)**.

⭐ If you found this project useful, consider giving it a star.
