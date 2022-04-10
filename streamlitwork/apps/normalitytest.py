import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image 
import io


    
def app():

    def _max_width_():
        max_width_str = f"max-width: 1000px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )

    # Hide the Streamlit header and footer
    def hide_header_footer():
        hide_streamlit_style = """
                    <style>
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    # increases the width of the text and tables/figures
    _max_width_()

    # hide the footer 
    hide_header_footer()
    
      

    st.markdown("# Data Quality Checker")
    st.markdown("Check the basic quality of any dataset")
    st.markdown("---")

   
    st.markdown("---")
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
            #st.header("Dataset Details")
            #st.write(df.head(10))
            # Show the no of columns dataset
            # st.title("Columns in Dataset")
            # st.write(df.columns)

            
             #show data
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
                
            st.markdown("---")
            
            if st.checkbox('Rows & Columns size'):
                st.markdown("Number of rows and columns helps us to determine how large the dataset is.")
                st.text('(Rows,Columns)')
                st.write(df.shape)

            st.markdown("---")   
        
        
            
            #check for null values
            if st.checkbox('Missing Values'):
                st.markdown("Missing values are known as null or NaN values. Missing data tends to **introduce bias that leads to misleading results.**")

                st.write("Number of rows:", len(df))
                dfnull = df.isnull().sum()/len(df)*100
                totalmiss = dfnull.sum().round(2)
                st.write("Percentage of total missing values:",totalmiss)
                st.write(dfnull)
                if totalmiss <= 30:
                    st.success("Looks good! as we have less then 30 percent of missing values.")
                
                else:
                    st.success("Poor data quality due to greater than 30 percent of missing value.")
                
            

                st.markdown(" > Theoretically, 25 to 30 percent is the maximum missing values are allowed, there’s no hard and fast rule to decide this threshold. It can vary from problem to problem.")
                

            st.markdown("---")   


            #check for completeness ratio 
            if st.checkbox('Completeness Ratio'):
                st.markdown(" Completeness is defined as the ratio of non-missing values to total records in dataset.") 
                # st.write("Total data length:", len(df))
                nonmissing = (df.notnull().sum().round(2))
                completeness= round(sum(nonmissing)/len(df),2)
                st.write("Completeness ratio:",completeness)
                st.write(nonmissing)

                if completeness >= 0.80:
                    st.success("Looks good! as we have completeness ratio greater than 0.85.")
                
                else:
                    st.success("Poor data quality due to low completeness ratio( less than 0.85).")

            st.markdown("---")

            #check dupication rate
            if st.checkbox('Duplication Rate'):
                st.markdown(" Duplication rate is defined as the ratio of  number of duplicates to total records in dataset.") 
                
                duplicated = df.duplicated().sum()
                dupratio= round(duplicated/len(df),2)
                st.write("Duplication rate:",dupratio)
                st.markdown(" > There’s no hard and fast rule to decide the threshold. It can vary from problem to problem.")
            
                    
            st.markdown("---")

            #check for normality test
            if st.checkbox('Normality'):


                images=Image.open('n.png')
                st.image(images,width=600, caption="Image from ALVARO.")


                st.markdown("Normality tests are used to determine if a dataset is well-modeled by a normal distribution. For normality test we can use skewness technique which is a quantification of how much a distribution is pushed left or right, a measure of asymmetry in the distribution.")
                aa= pd.DataFrame(df).skew()
                normalityskew= round(aa.mean(),4)
                st.write("How far is my dataset from Normal Distribution:", normalityskew)

                if normalityskew == 0 :
                    st.success("Your dataset is in  Normal Distribution i.e mean, mode and median are all equal ")
                
                elif normalityskew > 0:
                    st.success("Positively Skew so Mean  >  Median  >  Mode")

                elif normalityskew < 0:
                    st.success("Negatively Skew so Mode  >  Median  > Mean")   


                st.markdown("---")
    else:
            st.info('Awaiting for CSV file to be uploaded. Please upload the dataset')
            if st.checkbox('Check the box to use Example Dataset', key='head'):
                # Example data
            
                def load_data():
                    a = pd.read_csv('newdata.csv')
                    return a
                df = load_data()
                st.write(df.head(10))
                # Show the no of columns dataset
                st.title("Columns in Dataset")
                st.write(df.columns)

                st.title("Summary Statment")
                st.write(df.describe())

                buffer = io.StringIO()
                df.info(buf=buffer)
                s = buffer.getvalue()
                st.header('Detail Info of the Dataset')
                st.text(s)
            st.markdown("---")
            if st.checkbox('Rows & Columns size'):
                st.markdown("Number of rows and columns helps us to determine how large the dataset is.")
                st.text('(Rows,Columns)')
                st.write(df.shape)

            st.markdown("---")   
        
        
            
            #check for null values
            if st.checkbox('Missing Values'):
                st.markdown("Missing values are known as null or NaN values. Missing data tends to **introduce bias that leads to misleading results.**")

                st.write("Number of rows:", len(df))
                dfnull = df.isnull().sum()/len(df)*100
                totalmiss = dfnull.sum().round(2)
                st.write("Percentage of total missing values:",totalmiss)
                st.write(dfnull)
                if totalmiss <= 30:
                    st.success("Looks good! as we have less then 30 percent of missing values.")
                
                else:
                    st.success("Poor data quality due to greater than 30 percent of missing value.")
                
            

                st.markdown(" > Theoretically, 25 to 30 percent is the maximum missing values are allowed, there’s no hard and fast rule to decide this threshold. It can vary from problem to problem.")
                

            st.markdown("---")   


            #check for completeness ratio 
            if st.checkbox('Completeness Ratio'):
                st.markdown(" Completeness is defined as the ratio of non-missing values to total records in dataset.") 
                # st.write("Total data length:", len(df))
                nonmissing = (df.notnull().sum().round(2))
                completeness= round(sum(nonmissing)/len(df),2)
                st.write("Completeness ratio:",completeness)
                st.write(nonmissing)

                if completeness >= 0.80:
                    st.success("Looks good! as we have completeness ratio greater than 0.85.")
                
                else:
                    st.success("Poor data quality due to low completeness ratio( less than 0.85).")

            st.markdown("---")

            #check dupication rate
            if st.checkbox('Duplication Rate'):
                st.markdown(" Duplication rate is defined as the ratio of  number of duplicates to total records in dataset.") 
                
                duplicated = df.duplicated().sum()
                dupratio= round(duplicated/len(df),2)
                st.write("Duplication rate:",dupratio)
                st.markdown(" > There’s no hard and fast rule to decide the threshold. It can vary from problem to problem.")
            
                    
            st.markdown("---")

            #check for normality test
            if st.checkbox('Normality'):


                images=Image.open('n.png')
                st.image(images,width=600, caption="Image from ALVARO.")


                st.markdown("Normality tests are used to determine if a dataset is well-modeled by a normal distribution. For normality test we can use skewness technique which is a quantification of how much a distribution is pushed left or right, a measure of asymmetry in the distribution.")
                aa= pd.DataFrame(df).skew()
                normalityskew= round(aa.mean(),4)
                st.write("How far is my dataset from Normal Distribution:", normalityskew)

                if normalityskew == 0 :
                    st.success("Your dataset is in  Normal Distribution i.e mean, mode and median are all equal ")
                
                elif normalityskew > 0:
                    st.success("Positively Skew so Mean  >  Median  >  Mode")

                elif normalityskew < 0:
                    st.success("Negatively Skew so Mode  >  Median  > Mean")   


                st.markdown("---")    

   




    

  









     
