#import libraries
import pandas as pd #for file read and data manipulation
import numpy as np #for numeric calculations
import streamlit as st #for interactive dashboard
import joblib #to load model
import plotly.express as px #for interactive data visualization

#page settings
st.set_page_config(
    page_title='Iris Flower Dashboard',
    page_icon='🌸',
    layout='wide'
)

#load dataset
df = pd.read_csv('Iris.csv')

#create copy
df_copy = df.copy()

#remove spaces
df_copy.columns = df_copy.columns.str.strip()

#remove unwanted column
if 'Id' in df_copy.columns:
    df_copy = df_copy.drop('Id', axis = 1)

#load model
model, le = joblib.load('iris_model.pkl')

#header
st.title('🌸 Iris Flower Classification Dashboard')
st.markdown("""
Predict Iris flower species using Machine Learning and explore flower patterns.
""")

st.markdown('---')

#sidebar

#header
st.sidebar.header('Flower Measurements')

#filters
sepal_length = st.sidebar.number_input(
    'Sepal Length',
    min_value = 0.0,
    value = 5.1
)
sepal_width = st.sidebar.number_input(
    'Sepal Width',
    min_value = 0.0,
    value = 3.5
)
petal_length = st.sidebar.number_input(
    'Petal Length',
    min_value = 0.0,
    value = 1.4
)
petal_width = st.sidebar.number_input(
    'Petal Width',
    min_value = 0.0,
    value = 0.2
)

#body

#prediction section
st.subheader("🔮 Species Prediction")
if st.sidebar.button('Predict'):
    input_data = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=[
            'SepalLengthCm',
            'SepalWidthCm',
            'PetalLengthCm',
            'PetalWidthCm'
        ])

    prediction = model.predict(input_data)
    predicted_species = le.inverse_transform(prediction)
    st.success(f'Predicted Species: {predicted_species[0]}')

st.markdown("---")

#dataset preview
st.subheader('Dataset Preview')
st.dataframe(df_copy.head())

st.markdown('---')

#KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        'Total Samples',
        len(df_copy)
    )

with col2:
    st.metric(
        'Features',
        len(df_copy.columns) - 1
    )

with col3:
    st.metric(
        'Species Count',
        df_copy['Species'].nunique()
    )

st.markdown("---")

#dataset info
st.subheader("Dataset Information")
col4, col5 = st.columns(2)

with col4:
    st.write("Shape")
    st.write(df_copy.shape)

with col5:
    st.write("Missing Values")
    st.write(df_copy.isnull().sum())

st.markdown("---")

#species distribution
st.subheader("Species Distribution")
fig1 = px.histogram(
    df_copy,
    x = 'Species',
    color = 'Species',
    title = 'Species Count'
)
st.plotly_chart(fig1, use_container_width = True)

st.markdown("---")

#correlation heatmap
st.subheader("Correlation Heatmap")
corr = df_copy.drop('Species', axis = 1).corr()
fig2 = px.imshow(
    corr,
    text_auto = True,
    title = 'Feature Relationship'
)
st.plotly_chart(fig2, use_container_width = True)

st.markdown("---")

#petal analysis
st.subheader('Petal Length VS Petal Width')
fig3 = px.scatter(
    df_copy,
    x = 'PetalLengthCm',
    y = 'PetalWidthCm',
    color = 'Species',
    title = 'Petal Comparison'
)
st.plotly_chart(fig3, use_container_width = True)

st.markdown("---")

#sepal analysis
st.subheader('Sepal Length Distribution')
fig4 = px.box(
    df_copy,
    x = 'Species',
    y = 'SepalLengthCm',
    color = 'Species'
)
st.plotly_chart(fig4, use_container_width = True)

st.markdown("---")

#pair plot replacement
st.subheader("Feature Relationship")
fig5 = px.scatter_matrix(
    df_copy,
    dimensions = [
        'SepalLengthCm',
        'SepalWidthCm',
        'PetalLengthCm',
        'PetalWidthCm'
    ],
    color = 'Species'
)
st.plotly_chart(fig5, use_container_width = True)

st.markdown("---")

#insights
st.subheader("Key Insights")
st.markdown("""
- Petal measurements are highly useful for species classification.
- Setosa is clearly separated from other species.
- Versicolor and Virginica share some similarities.
- Feature correlation helps understand flower patterns.
- Machine Learning can classify flowers with high accuracy.
""")

st.markdown("---")

#footer
st.markdown('<h3 style="text-align:center;color:#ffb6c1;">🌸 Made By Panthini Patel</h3>', unsafe_allow_html = True)
st.markdown('<p style="text-align:center;font-size:20px;">🚀 Made Using Streamlit</p>', unsafe_allow_html = True)