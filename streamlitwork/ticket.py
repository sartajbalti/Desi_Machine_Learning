from email import header
from msilib.schema import Feature
import streamlit as st 
import seaborn as sns 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Make container 
header = st.container()
data_sets = st.container()
features = st.container()
modeltraining = st.container()

with header:
    st.header("Kashti k App ")
    st.text("Is me hm kashti k test bnayan gay")

with data_sets:
    st.header("Kashti dhoop gya ")
    st.text("we will work with titanic data set")
    df = pd.read_csv('Sample.csv')
    df = df.dropna()
    st.write(df.head(10))
    st.subheader('Sambha, Ay o Sambha Kitny Airlines thy ')
    st.bar_chart(df['airline'].value_counts())

    # other plots 
    st.subheader('Class k hissan sy faraq')
    st.bar_chart(df['baggage_weight'].value_counts())

    st.bar_chart(df['price'].sample(10))

with features:
    st.header("Kashti k featurse ")
    st.text("aween bhoot sary features addd krty hain ")
    st.markdown('1. **Feature 1:** \n This will pata ni kia btaya ga' )
    st.markdown('2. **Feature 2:** \n This will pata ni kia btaya ga' )
    st.markdown('3. **Feature 3:** \n This will pata ni kia btaya ga' )

with modeltraining:
    st.header("Kashti k kia bana ?")
    st.text("is me hm apny parameters ko kam ya ziada krain gay")
    # Making columns 
    input, display = st.columns(2)
    # First column me selection points 
max_depth = input.slider("Select Baggage pieces", min_value = 1, max_value = 10, value = 1, step = 1)

 # n estimators
n_estimators = input.selectbox("How many tress it should have ? ", options =[50,100,200,300,"No limits"] )
# Adding List of features 
input.write(df.columns)
# Input features 
input_features = input.text_input("Which feature do you wan to select")
    #st.bar_chart(df[input_features].sample(10))


# Machine Learning model 
if n_estimators == 'No limits':
    model = RandomForestRegressor(max_depth= max_depth)
else:
    model = RandomForestRegressor(max_depth= max_depth, n_estimators=n_estimators)
# define X and Y 
x = df[[input_features]]
y = df[['price']]

model_fit = model.fit(x,y)
pred = model.predict(y)

# Display model metrices 
display.subheader("Mean absolute error of the model is ")
display.write(mean_absolute_error(y,pred))
display.subheader("Mean squares error of the model is ")
display.write(mean_squared_error(y,pred))
display.subheader("r2 Score of the model is ")
display.write(r2_score(y,pred))