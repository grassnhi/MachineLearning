import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

# st.markdown(
#     """
#     <style>
#         .main{
#         background-color: #FFFFFF;
#         }

#     </style>  
#     """,
#     unsafe_allow_html=True
#     )

def getData(fileName):
    VNI_data = pd.read_csv(fileName)
    return VNI_data

with header:
    st.title('Welcom to my web!')
    st.text('This is a test version of my assignment.')

with dataset:
    st.title('VNINDEX')
    st.text('This contains 400 stock codes but my ass will choose only 9 of them.')

    VNI_data = getData('https://raw.githubusercontent.com/grassnhi/AI_ML_DL/main/AppWeb/Data/VNI.csv')

    VNI_data["Price"] = VNI_data["Price"].str.replace(',', '').astype(float)
    VNI_data["Change %"] = VNI_data["Change %"].str.replace('%', '').astype(float)
    VNI_data["Open"] = VNI_data["Open"].str.replace(',', '').astype(float)
    VNI_data["High"] = VNI_data["High"].str.replace(',', '').astype(float)
    VNI_data["Low"] = VNI_data["Low"].str.replace(',', '').astype(float)
    VNI_data["Vol."] = VNI_data["Vol."].str.replace('K', '0')
    VNI_data["Vol."] = VNI_data["Vol."].str.replace('M', '0000')
    VNI_data["Vol."] = VNI_data["Vol."].str.replace('.', '').astype(float)

    st.subheader('Pick up the Volume of VNI stock')
    priceCount = pd.DataFrame(VNI_data['Vol.'].value_counts()).head(50)
    st.bar_chart(priceCount)

    st.write(px.data.gapminder())

with features:
    st.title('Datetime and stock price')

    st.markdown('* **First feature:** I choose it... I create it...')
    st.markdown('* **Second feature:** I choose it... I create it...')

with modelTraining:
    st.title('VNINDEX STOCK PRICE PREDICTION')
    st.text('Now, let build a predicting model!')

    selectionCol, displayCol = st.columns(2)

    maxDepth = selectionCol.slider('What shoube be the max-depth of this model?',
                        min_value=10, max_value=100, value=20, step=10)

    nEstimators = selectionCol.selectbox('How many?',
                                        options=[100, 200, 300, 'No limit'],
                                        index=0)

    inputFeatures = selectionCol.text_input('Which feature shoube be use as input?', 'Price')

    selectionCol.text('List of features:')
    selectionCol.write(VNI_data.columns)

    if nEstimators == 'No limit':
        regr = RandomForestRegressor(max_depth=maxDepth)
    else:
        regr = RandomForestRegressor(max_depth=maxDepth, n_estimators=nEstimators)

    X = VNI_data[[inputFeatures]]     
    y = VNI_data[['Price']]  

    regr.fit(X, y) 
    prediction = regr.predict(y) 

    displayCol.subheader('Mean absolute error:') 
    displayCol.write(mean_absolute_error(y, prediction)) 

    displayCol.subheader('Mean square error:') 
    displayCol.write(mean_absolute_error(y, prediction)) 

    displayCol.subheader('R square score:') 
    displayCol.write(mean_absolute_error(y, prediction)) 