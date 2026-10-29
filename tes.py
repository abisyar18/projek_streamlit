import streamlit as st

st.title("Contoh Program Streamlit")
with st.form(key="my_form"):
    name = st.text_input("Masukkan nama Anda:")
    kelamin = st.radio("Pilih jenis kelamin:", ("Laki-laki", "Perempuan"))
    submit = st.form_submit_button(label="Kirim")