import pandas as pd
import streamlit as st

data = pd.read_excel('./pages/source.xlsx')
unique_category = data['Category'].unique()
unique_store = data['Store'].unique()

selected_category = st.multiselect("Select Category",options = unique_category)
criteria1 = data['Category'].isin(selected_category)

selected_store = st.multiselect("Select Store",options = unique_store)
criteria2 = data['Store'].isin(selected_store)

criteria3 = data['Price'] > 25000
criteria4 = (data['Price'] > 15000) & (data['Price'] < 50000)
criteria5 = (criteria1) & (criteria2) & (criteria4)

data = data[criteria1]

#print(data[criteria5])
print(data[criteria5].sort_values('Price',ascending=True))
st.dataframe(data)
