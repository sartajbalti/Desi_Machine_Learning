# Import libraries 
from datetime import datetime
from turtle import width
import streamlit as st
import plotly.express as px 
import pandas as pd

# Import DataSet 
st.title('COVID Dataset')
df = pd.read_csv("newdata.csv")
df['new_cases']=df['new_cases'].astype(int)
st.write(df.head(10))
# Show the no of columns dataset
st.title("Columns in Dataset")
st.write(df.columns)

st.title("Summary Statment")
st.write(df.describe())



con = df['date'].unique().tolist()

#cont = st.selectbox("Select the date you want to plot ", con)

#df = df[df['date']== cont]
# Plotting 
fig = px.scatter(df, x='total_cases', y='total_deaths', size='new_cases', color='location', hover_name='location',
log_x=True, size_max = 1000, range_x=[100,10000000], range_y =[100,2000], animation_frame='date',animation_group = 'location')
fig.update_layout(width=800, height=600)
st.write(fig)

