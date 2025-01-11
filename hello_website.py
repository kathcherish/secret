import streamlit as st
st.title("Welcome to This Page! *jan[new]ary secret yey!!*")
button = st.button("Look at this new feature")
button2 = st.button("Another feature!")
button3 = st.button("CURIOUS ABOUT ANOTHER SECRET?")

if button:
    st.balloons()

if button2:
    st.snow()
    
if button3:
    st.write("2024 SECRET UNLOCKED. See ya on fe[bravo]ry! There will be more next month see ya soon!")
    st.balloons()
    st.snow()
    




