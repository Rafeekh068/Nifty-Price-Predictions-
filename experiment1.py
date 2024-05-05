import pandas as pd
import pickle
import streamlit as st
import numpy as np

f=[]
def main():


    st.title('Nifty prediction using historical data')

    nav =st.sidebar.radio("navigation",['prediction','contribution'])

    if nav=='prediction':
        open1 =st.number_input('enter open')
        high=st.number_input('enter high')
        low=st.number_input('enter low')
        close=st.number_input('enter close')

        f=[open1,high,low,close]

        model= pickle.load(open("nifty model.sav",'rb'))

        pred=st.button('predict')

        if pred:

            prediction1=model.predict([f])
            st.write('prediction using LR',prediction1)

    if nav=='contribution':

        st.header('contribute to our data set')

        date=st.text_input('date')
        open1 =st.number_input('enter open')
        high=st.number_input('enter high')
        low=st.number_input('enter low')
        close=st.number_input('enter close')


        if st.button('submit'):

            to_add = {'data':date,'open':open1,'high':high,'low':low,'close':close}

            to_add=pd.DataFrame(to_add,index=[0],)
            to_add.to_csv('venv//nifty_data.csv',mode='a',index=False,header=False)

            st.success('submitted')


main()




