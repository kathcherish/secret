import streamlit as st
import pandas as pd

df = pd.read_excel('sumber.xlsx.xlsx')

st.set_page_config(layout='wide')

st.title("Stylique.🌷")

data = pd.read_excel('./pages/sumber.xlsx.xlsx')
unique_category = data['Category'].unique()
minimum_price = data['Price'].min()
maximum_price = data['Price'].max()

selected_category = st.multiselect("Select Category",options=unique_category,default=unique_category)
selected_size = st.multiselect("Select Size", ["S", "M", "XL"])
price_point = st.slider("Price",min_value=minimum_price,max_value=maximum_price,value=maximum_price)
ncolumns = st.number_input("Column layout",min_value=1,value=4,step=1)

criteria1 = data['Category'].isin(selected_category)
criteria2 = data['Price'] <= price_point

if selected_size:
  size_pattern =
  

join_criteria = (criteria1) & (criteria2) & (criteria3) & (criteria4) & (criteria5) & (criteria6)

data = data[join_criteria]
data_count = len(data)

columns = st.columns(ncolumns)

for i in range(data_count):
  for c in range(ncolumns):
    if i%ncolumns == c:
      col = columns[c]
      with col:
        product_picture = data.iloc[i]['Picture']
        product_name = data.iloc[i]['Name']
        product_price = data.iloc[i]['Price']
        product_sizes = data.iloc[i]['Sizes']
        st.image(product_picture,width = 250)
        st.write(f'{product_name}')
        st.write(f'{product_price:#,}')

        btnc1,btnc2 = st.columns(2)
        with st.container():
          with btnc1:
            if st.button("Buy",key=str(i)):
              st.write("Thank you! Your things will be deliver soon!")

          with btnc2:
            if st.button("Add To Cart",key=str(i)+"b"):
              st.write("Added to cart successfully!")

