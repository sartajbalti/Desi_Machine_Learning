import streamlit as st
st.set_page_config(layout="wide")
from multiapps import MultiApp
from apps import (
    eda,
    Newapp,
    corr,
    normalitytest
)


apps = MultiApp()
# Add all your application here
apps.add_app("Plotly", Newapp.app)
apps.add_app("EDA Analysis", eda.app)
apps.add_app("Correlation", corr.app)
apps.add_app("Normality", normalitytest.app)
# The main app
apps.run()