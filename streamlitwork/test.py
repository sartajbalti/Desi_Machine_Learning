import streamlit as st 
import seaborn as sns 
st.header("App ny sehri krli hai kia ap ko pata hai ")

phool = sns.load_dataset('iris')
st.write(phool[['species', 'sepal_length','petal_length']].head(10))
st.bar_chart(phool[['sepal_length','petal_length']])
st.line_chart(phool[['sepal_length','petal_length']])
