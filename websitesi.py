import streamlit as st
import joblib
import pandas as pd
import numpy as np


import joblib


model_path = '/Users/dilaraselin/Desktop/222802026/eniyi.joblib'
model = joblib.load(model_path)


st.title('Cep Telefonu Fiyat Tahmin Uygulaması')

st.header('Telefon Özelliklerini Giriniz')

ram = st.number_input('RAM Kapasitesi (GB)', min_value=1, max_value=16, step=1)
kamera_cozunurlugu = st.number_input('Kamera Çözünürlüğü (MP)', min_value=8, max_value=108, step=1)
dahili_hafiza = st.number_input('Dahili Hafıza (GB)', min_value=16, max_value=1000, step=16)
on_kamera_cozunurlugu = st.number_input('Ön Kamera Çözünürlüğü (MP)', min_value=5, max_value=64, step=1)
isletim_sistemi = st.selectbox('İşletim Sistemi', ['Android', 'iOS'])
sarj_hizi = st.number_input('Şarj Hızı (W)', min_value=0, step=1)

isletim_sistemi = 0 if isletim_sistemi == 'Android' else 1
user_input = pd.DataFrame({
    'RAM Kapasitesi': [ram],
    'Kamera Çözünürlüğü': [kamera_cozunurlugu],
    'Dahili Hafıza': [dahili_hafiza],
    'Ön Kamera Çözünürlüğü': [on_kamera_cozunurlugu],
    'İşletim Sistemi': [isletim_sistemi],
    'Şarj Hızı': [sarj_hizi]  
})





if st.button('Fiyatı Tahmin Et'):
    
    tahmin_fiyat = model.predict(user_input) * 1000
    st.subheader(f'Tahmin Edilen Fiyat: {tahmin_fiyat[0]:.2f} TL')

