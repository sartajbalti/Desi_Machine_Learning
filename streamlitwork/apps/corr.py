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
        # **Find the Correlation Along with the Visualization Just in one Click**
    
# Correlation 

What is Correlation?

Variables within a dataset can be related for lots of reasons.

Types:
- Pearson's
- Spearman's rho
- kendall's tau

For example:
- One variable could cause or depend on the values of another variable.
- One variable could be lightly associated with another variable.
- Two variables could depend on a third unknown variable.

**Positive Correlation:** both variables change in the same direction.

**Neutral Correlation:** No relationship in the change of the variables.

**Negative Correlation:** variables change in opposite directions.
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
                
            st.markdown("---")
            
            #btn1 = st.button('Press to click here to find the Correlation', key='cor')
            # btn2 = st.button('Click for Pearson Correlation', key='pears')
            # btn3=st.button('Click for Spearsman Correlation', key='spear')
            # btn4 = st.button('Click for Regplot', key='reg')
            
            #if btn1:
            st.header("Correllation")
            cor = df.corr()
            st.write(cor)
            
                #if btn2:
            Correlation_name = st.selectbox('Select Correlation type',('pearson','spearman','kendall'))
            if st.checkbox("Correlation",value=False):
                st.header("Shows the result of selected Correllation")
                corr1 =df.corr(method=Correlation_name)
                st.write(corr1)
            if st.checkbox("Ploty heatmap",value=False, key='plot'):
                st.header("heat Map of  above Selected Correllation")
                fig = px.imshow(corr1, text_auto=False)
                st.write(fig)
            if st.checkbox("Cool warm heatmap",value=False, key='he'):
                st.header("Cool Warm Heatmap Correlation")
                st.write(corr1.style.background_gradient('coolwarm'))
            if st.checkbox("Correlation Regress Plot",value=False, key='regss'):
                st.header("Select the values to check the Correlation using regress line to check +ive or -ive")
                abc = df.columns
                reg = st.selectbox('Select the value for x',abc)
                reg1 = st.selectbox('Select the value for y',abc)
                fig = px.scatter(
                        df, x=reg, y=reg1, opacity=0.65,
                        trendline='ols', trendline_color_override='darkblue'
                    )
                st.write(fig)
            if st.checkbox("Seaborn Pairplot",value=False):
                abcd = df.columns
                reg2 = st.selectbox('Select the value for x',abcd, key='inside')
                fig = sns.pairplot(df, hue=reg2) 
                st.pyplot(fig)  
            if st.checkbox("Seaborn Pairplot with Histogram",value=False):
                a = df.columns
                reg3 = st.selectbox('Select the value for x',a, key='in')
                fig = sns.pairplot(df, hue=reg3,diag_kind='hist' ) 
                st.pyplot(fig)   

            if st.checkbox("Seaborn Pairplot with Histogram without corners",value=False,):
                ax = df.columns
                reg4 = st.selectbox('Select the value for x',ax, key='ins')
                fig = sns.pairplot(df, hue=reg4,diag_kind='hist', corner=True ) 
                st.pyplot(fig)   
            if st.checkbox("Pair Plot",value=False):
                fig = sns.pairplot(cor)
                st.pyplot(fig)
        
            

        else:
            st.info('Awaiting for CSV file to be uploaded. Please upload the dataset')
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
            #btn1 = st.button('Press to click here to find the Correlation', key='cor')
            # btn2 = st.button('Click for Pearson Correlation', key='pears')
            # btn3=st.button('Click for Spearsman Correlation', key='spear')
            # btn4 = st.button('Click for Regplot', key='reg')
            #if btn1:
                st.header("Correllation")
                cor = df.corr()
                st.write(cor)
            
                            #if btn2:
                Correlation_name = st.selectbox('Select Correlation type',('pearson','spearman','kendall'))
                if st.checkbox("Correlation",value=False):
                    st.header("Shows the result of selected Correllation")
                    corr1 =df.corr(method=Correlation_name)
                    st.write(corr1)
                if st.checkbox("Ploty heatmap",value=False, key='plot'):
                    st.header("heat Map of  above Selected Correllation")
                    fig = px.imshow(corr1, text_auto=False)
                    st.write(fig)
                if st.checkbox("Cool warm heatmap",value=False, key='he'):
                    st.header("Cool Warm Heatmap Correlation")
                    st.write(corr1.style.background_gradient('coolwarm'))
                if st.checkbox("Correlation Regress Plot",value=False, key='regss'):
                    st.header("Select the values to check the Correlation using regress line to check +ive or -ive")
                    abc = df.columns
                    reg = st.selectbox('Select the value for x',abc)
                    reg1 = st.selectbox('Select the value for y',abc)
                    fig = px.scatter(
                            df, x=reg, y=reg1, opacity=0.65,
                            trendline='ols', trendline_color_override='darkblue'
                        )
                    st.write(fig)
                if st.checkbox("Seaborn Pairplot",value=False):
                    abcd = df.columns
                    reg2 = st.selectbox('Select the value for x',abcd, key='inside')
                    fig = sns.pairplot(df, hue=reg2) 
                    st.pyplot(fig)  
                if st.checkbox("Seaborn Pairplot with Histogram",value=False):
                    a = df.columns
                    reg3 = st.selectbox('Select the value for x',a, key='in')
                    fig = sns.pairplot(df, hue=reg3,diag_kind='hist' ) 
                    st.pyplot(fig)   

                if st.checkbox("Seaborn Pairplot with Histogram without corners",value=False,):
                    ax = df.columns
                    reg4 = st.selectbox('Select the value for x',ax, key='ins')
                    fig = sns.pairplot(df, hue=reg4,diag_kind='hist', corner=True ) 
                    st.pyplot(fig)   
                if st.checkbox("Pair Plot",value=False):
                    fig = sns.pairplot(cor)
                    st.pyplot(fig)
            