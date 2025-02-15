import pandas as pd
import streamlit as st

data = pd.read_excel('./pages/source.xlsx')
unique_category = data['Category'].unique()
unique_store = data['Store'].unique()
minimum_price = data['Price'].min()
maximum_price = data['Price'].max()

selected_category = st.multiselect("Select Category",options=unique_category,default=unique_category)
selected_store = st.multiselect("Select Store",options=unique_store,default=unique_store)
price_point = st.slider("Price",min_value=minimum_price,max_value=maximum_price,value=maximum_price)

criteria1 = data['Category'].isin(selected_category)
criteria2 = data['Store'].isin(selected_store)
criteria3 = data['Price'] <= price_point

join_criteria = (criteria1) & (criteria2) & (criteria3)

with st.container(border=True):
  data = data[join_criteria]
  data_count = len(data)
  for i in range(data_count):
    product_picture = data.iloc[i]['Picture']
    st.image(product_picture,width = 250)

    product_store = data.iloc[i]['Store']
    st.write(product_store)
    
    product_price = data.iloc[i]['Price']
    st.write(product_price)
    
  st.dataframe(data,use_container_width=True)
