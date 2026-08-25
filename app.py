import streamlit as st

st.title("My first dashboard")
st.write("If the slider moves the number, everything works.")

n = st.slider("Move me", 0, 100, 25)
st.metric("You picked", n)
st.write("Doubled:", n * 2)
