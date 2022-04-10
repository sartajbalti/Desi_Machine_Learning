import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **The Exprolatory Data Analysis Web App**
This is the **EDA App** created in Streamlit using the **pandas-profiling** library.
**Credit:** App built in `Python` + `Streamlit` by [Sartaj AHmed]
---
''')

# Upload CSV file From PC 
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://github.com/sartajbalti/Desi_Machine_Learning/blob/master/streamlitwork/Iris.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    
    st.write('---')
    st.header('**Pandas Profiling Report**')
   
    st_profile_report(pr)
    st.write('---')
    st.write(df.columns)
else:
    st.info('Awaiting for CSV file to be uploaded. Hun krdo upload file kam karny k lea bhaee')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.read_csv('Iris.csv')
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)