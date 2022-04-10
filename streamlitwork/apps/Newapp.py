import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px 
import statsmodels.api as sm 
import io


def app():
        # Web App Title
        st.markdown('''
        # **The Plotly Web App**
        This is the **plotly App** 
        **Credit:** App built in `Python` + `Streamlit` by [Sartaj AHmed]
        ---
        ''')

        # Upload CSV file From PC 
        st.header("Ulpoad you csv File")
        uploaded_file2 = st.file_uploader("Upload your input CSV file", type=["csv"])
        st.markdown("""
        [Example CSV input file](https://github.com/sartajbalti/Desi_Machine_Learning/blob/master/streamlitwork/Iris.csv)
        """)
        if uploaded_file2 is not None:
            
            def load_csv():
                csv = pd.read_csv(uploaded_file2)
                return csv
            df = load_csv()
            if st.checkbox('Show  Dataset'):
                num=st.number_input('No. of Rows',5,10)
                head=st.radio('View from top (head) or bottom (tail)',('Head','Tail'))
                
                if head=='Head':
                    st.dataframe(df.head(num))
                    st.title("Summary Statment")
                    st.write(df.describe())
                    buffer = io.StringIO()
                    df.info(buf=buffer)
                    s = buffer.getvalue()
                    st.text(s)
                else:
                    st.dataframe(df.tail(num))


            st.header("Using Plotly you can make animmation plot by selecting the values according to the data set")
            con = df.columns

            x = st.selectbox("Select the value for x  ", con)
            y = st.selectbox("Select the value for y  ", con)
            s = st.selectbox("Select the value for Size  ", con)
            c = st.selectbox("Select the value for color   ", con)
            h = st.selectbox("Select the value for hover   ", con)
            ag = st.selectbox("Select the value for Animation group", con)
            af = st.selectbox("Select the value for Animation frame", con)


            #df = df[df['date']== cont]
            # Plotting 
            fig = px.scatter(df, x=x, y=y, size=s, color=c, hover_name = h ,
            log_x=True, size_max = 1000, range_x=[100,10000000], range_y =[100,2000], animation_frame=af,animation_group = ag)
            fig.update_layout(width=800, height=600)
            st.write(fig)
            if st.checkbox('Check the box to click here to make a histogram', key='hi'):
                st.header("Please Select the value to make a Histogram")
                con1 = df.columns
                z = st.selectbox("Select the value for x  ", con1, key='hist')
                st.markdown("**Stacked values in Histogram In plotly different values can be shown in one column by using the color argument.**")
                f= st.selectbox("Select the value for Color  ", con1, key='hist')
                fig1 = px.histogram(df, x=z, color = f)
                st.write(fig1)
                

        else:
            st.info('Awaiting for CSV file to be uploaded. Hun krdo upload file kam karny k lea bhaee')
            if st.checkbox('Check the box to use Example Dataset', key='head'):
                # Example data
                def load_data():
                    a = pd.read_csv('newdata.csv')
                    return a
                df = load_data()
                if st.checkbox('Show  Dataset'):
                    num=st.number_input('No. of Rows',5,10)
                    head=st.radio('View from top (head) or bottom (tail)',('Head','Tail'))
                
                    if head=='Head':
                        st.dataframe(df.head(num))
                        st.title("Summary Statment")
                        st.write(df.describe())
                        buffer = io.StringIO()
                        df.info(buf=buffer)
                        s = buffer.getvalue()
                        st.text(s)
                    else:
                        st.dataframe(df.tail(num))



                fig = px.scatter(df, x='total_cases', y='total_deaths', size='new_cases', color='location', hover_name='location',
                log_x=True, size_max = 1000, range_x=[100,10000000], range_y =[100,2000], animation_frame='date',animation_group = 'location')
                fig.update_layout(width=800, height=600)
                st.write(fig)
                if st.checkbox('Check the box to click here to make a histogram', key='hi'):
                    st.header("Please Select the value to make a Histogram")
                    con1 = df.columns
                    z = st.selectbox("Select the value for x  ", con1, key='hist')
                    fig1 = px.histogram(df, x=z)
                    st.write(fig1)
                