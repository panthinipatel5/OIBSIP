#import libraries
import streamlit as st #for interactive dashboard
import pandas as pd #for file read and data manipulation
import numpy as np #for numeric calculation
import plotly.express as px #for interactive visualization
import joblib #to load model

#page settings
st.set_page_config(
    page_title = 'Car Price Prediction Dashboard',
    page_icon = '🚗',
    layout = 'wide'
)

#load model
model = joblib.load("car_price_model.pkl")

#load dataset (optional for dashboard visuals)
df = pd.read_csv("car data.csv")

#create copy
df_copy = df.copy()


#header

#title
st.title("🚗 Car Price Prediction Dashboard")

#description
st.markdown("""
Predict used car prices using Machine Learning and explore car market insights.
""")

st.markdown("---")

#sidebar


#sidebar header
st.sidebar.header("Filters")

#filters
selected_fuel = st.sidebar.selectbox(
    "Fuel Type",
    ["All"] + list(df_copy["Fuel_Type"].unique())
)

selected_seller = st.sidebar.selectbox(
    "Seller Type",
    ["All"] + list(df_copy["Selling_type"].unique())
)

#filtering
filter_df = df_copy.copy()

if selected_fuel != "All":
    filter_df = filter_df[filter_df["Fuel_Type"] == selected_fuel]

if selected_seller != "All":
    filter_df = filter_df[filter_df["Selling_type"] == selected_seller]

#body

#data preview
st.subheader("Data Preview")
st.dataframe(filter_df.head())

st.markdown("---")

#KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Car Price",
        f"₹ {round(filter_df['Selling_Price'].mean(),2)} L"
    )

with col2:
    st.metric(
        "Average Present Price",
        f"₹ {round(filter_df['Present_Price'].mean(),2)} L"
    )

with col3:
    st.metric(
        "Average KMs Driven",
        int(filter_df['Driven_kms'].mean())
    )

st.markdown("---")

#data visualizations

st.subheader("Selling Price Distribution")
fig1 = px.histogram(
    filter_df,
    x = "Selling_Price",
    nbins = 30,
    title = "Distribution of Car Prices"
)
st.plotly_chart(fig1, use_container_width = True)

st.markdown("---")

st.subheader("Fuel Type Analysis")
fuel_data = filter_df.groupby("Fuel_Type")["Selling_Price"].mean().reset_index()
fig2 = px.bar(
    fuel_data,
    x = "Fuel_Type",
    y = "Selling_Price",
    title = "Average Price by Fuel Type"
)
st.plotly_chart(fig2, use_container_width = True)

st.markdown("---")

st.subheader("Transmission Analysis")
fig3 = px.box(
    filter_df,
    x = "Transmission",
    y = "Selling_Price",
    color = "Transmission",
    title = "Manual VS Automatic"
)
st.plotly_chart(fig3, use_container_width = True)

st.markdown("---")

st.subheader("Year Wise Price Trend")
year_data = filter_df.groupby("Year")["Selling_Price"].mean().reset_index()
fig4 = px.line(
    year_data,
    x = "Year",
    y = "Selling_Price",
    title = "Price Trend Over Years"
)
st.plotly_chart(fig4, use_container_width = True)

st.markdown("---")

#correlation heatmap

st.subheader("Correlation Heatmap")
corr = filter_df.select_dtypes(include = np.number).corr()
fig5 = px.imshow(
    corr,
    text_auto = True,
    title = "Numerical Feature Relationship"
)
st.plotly_chart(fig5, use_container_width = True)

st.markdown("---")

#prediction section

st.subheader("🔮 Car Price Prediction")
year = st.number_input("Year", 2000, 2025, 2015)
present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0, 5.0)
kms = st.number_input("Driven KMs", 0, 200000, 30000)
fuel = st.selectbox("Fuel Type", ["Petrol","Diesel","CNG"])
seller = st.selectbox("Seller Type", ["Dealer","Individual"])
trans = st.selectbox("Transmission", ["Manual","Automatic"])

#mapping
fuel_map = {
    "Petrol":0,
    "Diesel":1,
    "CNG":2
}
seller_map = {
    "Dealer":0,
    "Individual":1
}
trans_map = {
    "Manual":0,
    "Automatic":1
}

if st.button("Predict Price"):

    input_data = np.array([[
        year,
        present_price,
        kms,
        fuel_map[fuel],
        seller_map[seller],
        trans_map[trans]
    ]])

    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: ₹ {prediction : .2f} Lakhs")

st.markdown("---")

#insights
st.subheader("Key Insights")

st.markdown("""
- Diesel cars usually retain better resale value.
- Lower driven kilometers increase resale prices.
- Automatic cars often have higher market value.
- Car age strongly affects resale value.
- Machine Learning improves price estimation accuracy.
""")

st.markdown("---")

#footer
st.markdown('<h3 style = "text-align : center; color : #ffb6c1;">🌸 Made By Panthini Patel</h3>', unsafe_allow_html = True)
st.markdown('<p style = "text-align : center; font-size : 20px;">🚀 Made Using Streamlit</p>', unsafe_allow_html = True)
