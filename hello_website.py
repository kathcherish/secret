import streamlit as st
st.title("Welcome to This Page! *jan[new]ary secret yey!!*")
button = st.button("Look at this new feature")
button2 = st.button("Another feature!")
button3 = st.button("CURIOUS FOR THIS LAST ONE?")

if button:
    st.balloons()

if button2:
    st.snow()
    
if button3:
    st.write("1/10 of 2025 SECRET UNLOCKED. See ya on fe[bravo]ry!")
    st.balloons()
    st.snow()
    




