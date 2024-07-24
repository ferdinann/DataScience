import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
dataDay = pd.DataFrame(pd.read_csv('day.csv'))
dataHour = pd.DataFrame(pd.read_csv('hour.csv'))

st.title('Dashboard Proyek analisis data')
st.text("Dataset day.csv")
st.dataframe(data=dataDay,width=700,height=200)

st.text("Dataset hour.csv")
st.dataframe(data=dataDay,width=700,height=200)

st.text('Permintaan sewa sepeda berdasarkan hari')
if 'cnt' in dataDay.columns:  
  fig, ax = plt.subplots()
  ax.bar(x=dataDay['weekday'], height=dataDay['cnt'])
  ax.set_title('Permintaan sewa sepeda per hari')
  ax.set_xlabel('Hari')
  ax.set_ylabel('Jumlah')
  st.pyplot(fig)  
else:
   st.error("Data tidak ditemukan")

st.text('Permintaan sewa sepeda berdasarkan jam')
if 'cnt' in dataHour.columns:  
  fig, ax = plt.subplots()
  ax.bar(x=dataHour['hr'], height=dataHour['cnt']) 
  ax.set_title('Permintaan sewa sepeda per jam')
  ax.set_xlabel('Jam')
  ax.set_ylabel('Jumlah')
  st.pyplot(fig)   
else:
   st.error("Data tidak ditemukan")

st.text('Permintaan sewa sepeda berdasarkan musim')
if 'cnt' in dataDay.columns:  
  fig, ax = plt.subplots()
  ax.bar(x='season',data= dataDay,height='cnt') 
  ax.set_title('Permintaan sewa sepeda per musim')
  ax.set_xlabel('Musim')
  ax.set_ylabel('Jumlah')
  st.pyplot(fig)  
else:
   st.error("Data tidak ditemukan")


st.text('Permintaan sewa sepeda berdasarkan cuaca')
if 'cnt' in dataDay.columns:  
  fig, ax = plt.subplots()
  ax.bar(x='weathersit',data= dataDay,height='cnt') 
  ax.set_title('Permintaan sewa sepeda per cuaca')
  ax.set_xlabel('Cuaca')
  ax.set_ylabel('Jumlah')
  st.pyplot(fig)  
else:
   st.error("Data tidak ditemukan")

st.text('Kelompok pengguna yang memakai jasa sewa sepeda')
if 'cnt' in dataDay.columns:  
  fig, ax = plt.subplots()
  ax.pie(x=[dataDay['casual'].sum(),dataDay['registered'].sum()],labels=['casual','registered'],autopct='%1.1f%%') 
  st.pyplot(fig)   
else:
  st.error("Data tidak ditemukan")

    
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
