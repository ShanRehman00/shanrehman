# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:12:54 2022

@author: Shan Rehman
"""

import streamlit as st
import pandas as pd
df = pd.read_csv(r"C:\Users\Shan Rehman\Downloads\AirPassengers.csv")
print(df)

def main():
    st.title("Air Passengers Analysis")
    selection = st.selectbox('Select period', df['Month'])
    st.text(df['#Passengers'][df['Month']==selection])
    
    
if __name__=='__main__':
    main()
    
    
    