import streamlit as st
start_color, end_color = st.select_slider(
     'Select a range of color wavelength',
     options=[i for i in range(1,100)],
     value=(1, 100))
st.write('You selected wavelengths between', start_color, 'and', end_color)
