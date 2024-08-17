
import streamlit as st
import time

st.title("To jest strona Iwony Milewskiej")
col1, col2 = st.columns([1, 1])

uploades_photo = col2.file_uploader("Upload a photo")
# col1.image("media/Iwonka_plaza_siedzaca_Emilia_1115 × 1672.jpg")
