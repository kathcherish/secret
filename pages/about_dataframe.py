import pandas as pd
import streamlit as st

data = pd.read_excel('./pages/source.xlsx')
unique_category = data['Category'].unique()
unique_store = data['Store'].unique()
minimum_price = data['Price'].min()
maximum_price = data['Price'].max()

selected_category = st.multiselect("Select Category",options=unique_Category,default=unique_Category)
selected_store = st.multiselect("Select Store",options=unique_Store,default=unique_Store)
price_point = st.slider("Price",min_value=minimum_Price,max_value=maximum_Price,value=maximum_Price)

criteria1 = data['Category'].isin(selected_category)
criteria2 = data['Store'].isin(selected_store)
criteria3 = data['Price'] <= price_point

join_criteria = (criteria1) & (criteria2) & (criteria3)

with st.container(border=True):
  data = data[join_criteria]
  st.dataframe(data,use_container_width=True)
