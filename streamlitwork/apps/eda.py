import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
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
        # Web App Title
        st.title("The EDA Analysis")
        st.markdown('''
        # **The Exprolatory Data Analysis Web App**
        ---
        ''')

        # Upload CSV file From PC with st.sidebar.header('1. Upload your CSV data'):
        st.header("Upload you csv File")
        uploaded_file1 = st.file_uploader("Upload your input CSV file", type=["csv"])
        st.markdown("""
        [Example CSV input file](https://github.com/sartajbalti/Desi_Machine_Learning/blob/master/streamlitwork/Iris.csv)
        """)

        # Pandas Profiling Report
        if uploaded_file1 is not None:
            @st.cache
            def load_csv():
                csv = pd.read_csv(uploaded_file1)
                return csv
            df = load_csv()
            pr = ProfileReport(df, explorative=True)
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
                
            if st.checkbox('Show  Pandas Profiling Report'):
            
                st.write('---')
                st.header('**Pandas Profiling Report**')
            
                st_profile_report(pr)
                st.write('---')
        else:
            st.info('Awaiting for CSV file to be uploaded. Hun krdo upload file kam karny k lea bhaee')
            if st.checkbox('Check the box to use Example Dataset', key='head'):
                # Example data
                @st.cache
                def load_data():
                    a = pd.read_csv('newdata.csv')
                    return a
                df = load_data()
                pr = ProfileReport(df, explorative=True)
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
                
                if st.checkbox('Show  Pandas Profiling Report'):
            
                    st.write('---')
                    st.header('**Pandas Profiling Report**')
                
                    st_profile_report(pr)
                    st.write('---')