#import libraries
import streamlit as st #for interactive dashboard
import pandas as pd #for file read and data manipulation
import numpy as np #for numeric calculations
import joblib #to load model
import plotly.express as px #for interactive data visualization

#page settings
st.set_page_config(
    page_title='Sales Prediction Dashboard',
    page_icon='📈',
    layout='wide'
)

#load data
df = pd.read_csv("Advertising.csv")

#create copy
df_copy = df.copy()

#remove spaces if any
df_copy.columns = df_copy.columns.str.strip()

#load model
model = joblib.load("sales_model.pkl")

#header

#title
st.title("📈 Sales Prediction Dashboard")

st.markdown("""
Predict product sales using Machine Learning and analyze advertisement impact.
""")

st.markdown("---")

#sidebar

#header
st.sidebar.header("Advertisement Budget")

tv = st.sidebar.slider(
    "📺 TV Budget",
    0.0,
    300.0,
    150.0
)

radio = st.sidebar.slider(
    "📻 Radio Budget",
    0.0,
    50.0,
    25.0
)

newspaper = st.sidebar.slider(
    "📰 Newspaper Budget",
    0.0,
    120.0,
    30.0
)

st.sidebar.markdown("---")

st.sidebar.info("""
Adjust advertisement budgets and predict expected sales.
""")

#body

#prediction
input_data = np.array([
    [tv, radio, newspaper]
])
prediction = model.predict(input_data)

#prediction output
st.subheader("🔮 Sales Prediction")
st.success(f"Estimated Sales: {prediction[0] : .2f}")

st.markdown("---")

#dataset preview
st.subheader("Dataset Preview")
st.dataframe(df_copy.head())

st.markdown("---")

#KPI section
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average TV Budget",
        round(df_copy["TV"].mean(),2)
    )

with col2:
    st.metric(
        "Average Radio Budget",
        round(df_copy["Radio"].mean(),2)
    )

with col3:
    st.metric(
        "Average Sales",
        round(df_copy["Sales"].mean(),2)
    )

st.markdown("---")

#statistics
st.subheader("Statistical Summary")
st.dataframe(df_copy.describe())

st.markdown("---")

#heatmap
st.subheader("Correlation Heatmap")
corr = df_copy.corr()
fig1 = px.imshow(
    corr,
    text_auto = True,
    title = 'Relationship Between Features'
)
st.plotly_chart(fig1, use_container_width = True)

st.markdown("---")

#TV vs sales
st.subheader("📺 TV Advertisement vs Sales")
fig2 = px.scatter(
    df_copy,
    x = 'TV',
    y = 'Sales',
    trendline = 'ols',
    title = 'TV Budget Impact'
)
st.plotly_chart(fig2, use_container_width = True)

st.markdown("---")

#radio vs sales
st.subheader("📻 Radio Advertisement vs Sales")
fig3 = px.scatter(
    df_copy,
    x = 'Radio',
    y = 'Sales',
    trendline = 'ols',
    title = 'Radio Budget Impact'
)
st.plotly_chart(fig3, use_container_width = True)

st.markdown("---")

#newspaper vs sales
st.subheader("📰 Newspaper Advertisement vs Sales")
fig4 = px.scatter(
    df_copy,
    x = 'Newspaper',
    y = 'Sales',
    trendline = 'ols',
    title = 'Newspaper Budget Impact'
)
st.plotly_chart(fig4, use_container_width = True)

st.markdown("---")

#key insights
st.subheader("Key Insights")
st.markdown("""
- TV advertising usually has the strongest impact on sales.
- Radio marketing also contributes significantly.
- Newspaper ads often show weaker correlation.
- Higher ad budgets generally increase sales.
- Machine Learning helps estimate future sales trends.
""")

st.markdown("---")

#footer
st.markdown('<h3 style="text-align:center;color:#ffb6c1;">🌸 Made By Panthini Patel</h3>', unsafe_allow_html = True)
st.markdown('<p style="text-align:center;font-size:20px;">🚀 Made Using Streamlit</p>', unsafe_allow_html = True)