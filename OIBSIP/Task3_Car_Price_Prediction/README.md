# 🚗 Car Price Prediction using Machine Learning  
## Intelligent Vehicle Price Estimation System

An interactive Machine Learning project built using **Python**, **Scikit-learn**, and **Streamlit** to predict the selling price of used cars based on various vehicle features.  

The project combines **Exploratory Data Analysis (EDA)**, data visualization, predictive modeling, and an interactive dashboard to estimate car resale prices accurately.

---

# 🚀 Project Features

- 🚗 Used car price prediction system
- 📊 Interactive Streamlit dashboard
- 📈 Exploratory Data Analysis (EDA)
- 🔥 Correlation heatmap visualization
- 📉 Price distribution analysis
- 🤖 Machine Learning prediction model
- 📋 Dataset statistics and insights
- 🎯 Real-time car price prediction

---

# 📂 Dataset Information

The dataset contains information about different cars and their selling prices.

## 📌 Dataset Features

| Feature | Description |
|---|---|
| Car_Name | Name of the car |
| Year | Manufacturing year |
| Selling_Price | Selling price of the car |
| Present_Price | Current showroom price |
| Driven_kms | Total kilometers driven |
| Fuel_Type | Petrol / Diesel / CNG |
| Selling_type | Dealer or Individual |
| Transmission | Manual or Automatic |
| Owner | Number of previous owners |

---

# 🧠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

# 📊 Exploratory Data Analysis (EDA)

The project performs detailed data analysis including:

- Data cleaning
- Missing value checking
- Statistical summary
- Correlation analysis
- Price distribution visualization
- Feature relationship analysis

---

# 📈 Key Insights

- Most cars are priced below ₹10 Lakhs.
- Present price has a strong impact on selling price.
- Newer cars generally have higher resale value.
- Cars driven more kilometers usually have lower prices.
- Diesel vehicles often show better resale value.
- Automatic transmission cars are slightly more expensive.

---

# 🤖 Machine Learning Model

## ✅ Model Used
- Linear Regression

## ⚙️ ML Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Encoding
4. Exploratory Data Analysis
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Real-Time Prediction

---

# 📉 Model Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)

The model predicts car prices by learning relationships between vehicle features and selling prices.

---

# 🖥️ Interactive Streamlit Dashboard

The dashboard allows users to:

- Enter car details
- Select fuel and transmission type
- Predict selling price instantly
- Explore prediction results interactively

---

## 📂 Project Structure

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

# 💾 Model Saving

The trained model is saved using Joblib:

```python
joblib.dump(model, "car_price_model.pkl")
```

---

# 🌟 Future Improvements

- Random Forest & XGBoost Models
- Advanced Feature Engineering
- Better UI/UX Dashboard Design
- Real-Time Market Price Integration
- Deployment on Streamlit Cloud
- Advanced Data Visualizations

---

# 📜 License

This project is open-source and available for educational and learning purposes.

---

# 👨‍💻 Author

Panthini Patel
