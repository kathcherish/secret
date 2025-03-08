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
ncolumns = st.number_input("Column layout",min_value=1,value=4,step=1)

criteria1 = data['Category'].isin(selected_category)
criteria2 = data['Store'].isin(selected_store)
criteria3 = data['Price'] <= price_point

join_criteria = (criteria1) & (criteria2) & (criteria3)

data = data[join_criteria]
data_count = len(data)

for i in range(data_count):
  for c in range(ncolumns):
    if i%ncolumns == c:
      col = columns[c]
      with col:
        product_picture = data.iloc[i]['Picture']
        st.image(product_picture,width = 240)

    #product_name = data.iloc[i]['Name']
    #st.write(product_name)
    #product_price = data.iloc[i]['Price']

    btnc1,btnc2 = st.columns(2)
    with st.container():
      with btnc1:
        if st.button("Buy",key=str(i)):
          st.write("Thank you! Your things will be deliver soon!")

      with btnc2:
        if st.button("Add To Cart",key=str(i)+"b"):
          st.write("Added to cart successfully!")

  st.dataframe(data,use_container_width=True)
