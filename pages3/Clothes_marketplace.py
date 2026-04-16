import streamlit as st
import pandas as pd

df = pd.read_excel('sources1.xlsx')

with st.container(border=True):
    col1,col2,col3 = st.columns(3)
    
    with col1: 
        selected_Category = st.selectbox("Choose Category",
                                        options=df['Category'].unique())
    
    with col2:
        selected_Name = st.selectbox("Choose Name",
                                     options=df['Name'].unique())
    
    with col3:
        selected_Store = st.selectbox("Choose Store",
                                      options=df['Store'].unique())
        
    with col4:
        selected_Size1 = st.selectbox("Choose Size",
                                      options=df['Size1'].unique())
        
    with col5:
        selected_Size2 = st.selectbox("Choose Size",
                                      options=df['Size2'].unique())
        
    with col6:
        selected_Size3 = st.selectbox("Choose Size",
                                      options=df['Size3'].unique())
        

df = df[df['Category'] == selected_Category ]
df = df[df['Name'] == selected_Name ]
df = df[df['Store'] == selected_Store ]
df = df[df['Size1'] == selected_Size1 ]
df = df[df['Size2'] == selected_Size2 ]
df = df[df['Size3'] == selected_Size3 ]

st.dataframe(df)

