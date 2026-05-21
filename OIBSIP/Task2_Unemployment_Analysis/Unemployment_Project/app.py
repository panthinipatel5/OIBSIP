#import libraries
import pandas as pd #file read and data manipulation
import numpy as np #for numeric operations
import plotly.express as px #for interactive data visualization
from sklearn.preprocessing import StandardScaler #for encoding categorical to numerical data
from sklearn.model_selection import train_test_split #for spliting data into train and test sets
from sklearn.linear_model import LinearRegression #for numeric value prediction
from sklearn.impute import SimpleImputer #for handling missing values in ML model
from sklearn.pipeline import Pipeline #for combining multi steps in ML
import joblib #to load model
import streamlit as st #for interactive dashboard

#tab settings
st.set_page_config(
    page_title = 'Unemployment Analysis Dashboard',
    page_icon = '📊',
    layout = 'wide'
)

#load model
model = joblib.load('Unemployment_model.pkl')

#load dataset
df = pd.read_csv('Unemployment in India.csv')

#create a copy of dataset
df_copy = df.copy()

#remove extra spaces
df_copy.columns = df_copy.columns.str.strip()

#convert date column into proper date format
df_copy['Date'] = pd.to_datetime(df_copy['Date'], dayfirst = True)

#filling missing values 

#for numeric:
numeric_cols = df_copy.select_dtypes(include = np.number).columns
df_copy[numeric_cols] = df_copy[numeric_cols].fillna(df_copy[numeric_cols].median())

#for categorical:
categorical_cols = df_copy.select_dtypes(include = 'object').columns
df_copy[categorical_cols] = df_copy[categorical_cols].fillna(df_copy[categorical_cols].mode().iloc[0])

#feature extraction

#create month column
df_copy['Month'] = df_copy['Date'].dt.month

#create year column
df_copy['Year'] = df_copy['Date'].dt.year

#create copy of cleaned one
filter_df = df_copy.copy()

#header

#title
st.title('📊 Unemployment Analysis Dashboard')

#description
st.markdown("""
Analysis of Unemployment trends during Covid-19 using Machine Learning""")

#horizontal line
st.markdown('---')

#sidebar creation

#header
st.sidebar.header('Filters')

#dropdown

selected_state = st.sidebar.selectbox(
    'Select State',
    ['All'] + list(filter_df['Region'].unique())
)

selected_area = st.sidebar.selectbox(
    'Select Area',
    ['All'] + list(filter_df['Area'].unique())
)

#state filtering

if selected_state != 'All':
    filter_df = filter_df[filter_df['Region'] == selected_state]

#area filtering

if selected_area != 'All':
    filter_df = filter_df[filter_df['Area'] == selected_area]

#main body

#data preview
st.subheader('Data Preview')
st.dataframe(filter_df.head())

#KPI
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        'Average Unemployment Rate',
        round(filter_df['Estimated Unemployment Rate (%)'].mean(), 2)
    )

with col2:
    st.metric(
        'Average Employment',
        int(filter_df['Estimated Employed'].mean())
    )

with col3:
    st.metric(
        'Average Labour Participation',
        round(filter_df['Estimated Labour Participation Rate (%)'].mean(), 2)
    )

#horizontal line
st.markdown('---')

#data visuals

st.subheader('Unemployment Rate Distribution')
fig1 = px.histogram(
    filter_df, 
    x = 'Estimated Unemployment Rate (%)', 
    nbins = 30, 
    title = 'Distribution Of Unemployment Rate'
)
st.plotly_chart(fig1, use_container_width = True)

#horizontal line
st.markdown('---')

st.subheader('State Wise Unemployment Rate')
avg_unemployment = filter_df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().reset_index()
fig2 = px.bar(
    avg_unemployment, 
    x = 'Region', 
    y = 'Estimated Unemployment Rate (%)', 
    title = 'Average Unemployment By State'
)
st.plotly_chart(fig2, use_container_width = True)

#horizontal line
st.markdown('---')

st.subheader('Area Wise Unemployment Rate')
fig3 = px.box(
    filter_df,
    x = 'Area',
    y = 'Estimated Unemployment Rate (%)',
    color = 'Area',
    title = 'Rural VS Urban Unemployment'
)
st.plotly_chart(fig3, use_container_width = True)

#horizontal line
st.markdown('---')

st.subheader('Covid-19 Unemployment Trend')
trend_df = filter_df.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()
fig4 = px.line(
    trend_df,
    x =  'Date',
    y = 'Estimated Unemployment Rate (%)',
    title = 'Average Unemployment Trend Over Time'
)
st.plotly_chart(fig4, use_container_width = True)

#horizontal line
st.markdown('---')

st.subheader('Correlation Heatmap')
corr_matrix = filter_df.select_dtypes(include = np.number).corr()
fig5 = px.imshow(
    corr_matrix,
    text_auto = True,
    title = 'Relationship Strength Across Numerical Features'
)
st.plotly_chart(fig5, use_container_width = True)

#horizontal line
st.markdown('---')

#model handling for future prediction

#model training
features = [
    'Estimated Employed',
    'Estimated Labour Participation Rate (%)',
    'Month',
    'Year'
]

x = df_copy[features]
y = df_copy['Estimated Unemployment Rate (%)']

model = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy = 'median')),
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model.fit(x_train, y_train)

#prediction
y_prediction = model.predict(x_test)

#future Prediction
employed = st.number_input('Estimated Employed', value = 15000000)
labour = st.number_input('Estimated Labour Participation', value = 45.0)
month = st.slider('Month', 1, 12, 7)
year = st.slider('Year', 2027, 2047, 2032)

if st.button('Predict'):
    future_input = pd.DataFrame(
    [[employed,
     labour,
     month,
     year]],

    columns = [
    'Estimated Employed',
    'Estimated Labour Participation Rate (%)',
    'Month',
    'Year'
    ])
    
    future_predict = model.predict(future_input)
    st.success(f'Predicted Unemployment Rate: {round(future_predict[0], 2)} %')

#horizontal line
st.markdown('---')

#final Insights
st.subheader("Key Insights")

st.markdown("""
- Covid-19 significantly increased unemployment in India.
- Lockdowns caused sudden job losses across states.
- Urban and rural areas showed different impact patterns.
- Recovery varied by region and time.
- Machine Learning helps in forecasting trends effectively.
""")

#horizontal line
st.markdown('---')

#footer
st.markdown('<h3 style = "text-align : center; color : #ffb6c1">🌸 Made By Panthini Patel</h3>', unsafe_allow_html = True)
st.markdown('<p style = "text-align : center; font-size : 20px;">🚀 Made Using Streamlit</p>', unsafe_allow_html = True)