import streamlit as st

conversion_factors = {
  'distance': {'mm':1, 
               'cm':0.1,
               'm': 0.01},
  'calories': {'fries': 319,
               'donut': 190,
               'burger': 290,
               'ice cream': 207,
               'apple':52,
               'cabbage': 25,
               'banana': 88,
               'coke': 139,
               'milk': 42},
        

'weight':None,
'time':None
}

col1,col2,col3,col4,col5 = st.columns(5)

#selection category
with col1:
  category_list = list(conversion_factors.keys())
  category = st.radio("Select category",options=category_list)
  st.write(category_list)

with col2:
  st.write("Input Numbers")

with col3:
  base_unit_list = list(conversion_factors[category].keys())
  base_unit = st.radio("From",options=base_unit_list)
  st.write(base_unit_list)

with col4:
  target_unit_list = list(conversion_factors[category].keys())
  target_unit = st.radio("To",options=target_unit_list)
  st.write(target_unit_list)

with col5:
  st.write("Output Result")



