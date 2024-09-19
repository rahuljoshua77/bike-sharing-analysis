import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title('Bike Sharing Data Analysis Dashboard')

# Load dataset
df_day = pd.read_csv('day.csv')
df_hour = pd.read_csv('hour.csv')

# Sidebar untuk memilih data
dataset = st.sidebar.selectbox("Pilih dataset", ("Day", "Hour"))

# Menampilkan beberapa baris data
if dataset == "Day":
    st.subheader('Data Penyewaan Sepeda (Day)')
    st.write(df_day.head())
else:
    st.subheader('Data Penyewaan Sepeda (Hour)')
    st.write(df_hour.head())

# Visualisasi jumlah penyewaan berdasarkan suhu
st.subheader('Visualisasi Pengaruh Suhu Terhadap Jumlah Penyewaan')
fig, ax = plt.subplots()
if dataset == "Day":
    sns.scatterplot(x='temp', y='cnt', data=df_day, ax=ax)
else:
    sns.scatterplot(x='temp', y='cnt', data=df_hour, ax=ax)
ax.set_title('Pengaruh Suhu Terhadap Penyewaan')
ax.set_xlabel('Temperature (Normalized)')
ax.set_ylabel('Count of Rentals')
st.pyplot(fig)

# Visualisasi pola penyewaan berdasarkan jam
st.subheader('Visualisasi Pola Penyewaan Berdasarkan Jam')
if dataset == "Hour":
    fig, ax = plt.subplots()
    sns.lineplot(x='hr', y='cnt', data=df_hour, ax=ax)
    ax.set_title('Pola Penyewaan Berdasarkan Jam')
    ax.set_xlabel('Hour')
    ax.set_ylabel('Count of Rentals')
    st.pyplot(fig)
else:
    st.write("Pola ini hanya tersedia untuk data hourly.")

# Analisis RFM
st.subheader('Analisis RFM Sederhana')
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
max_date = df_day['dteday'].max()
df_day['recency'] = (max_date - df_day['dteday']).dt.days
df_day['frequency'] = df_day.groupby('yr')['cnt'].transform('sum')
df_day['monetary'] = df_day['cnt']

# Menampilkan scatter plot dari analisis RFM
fig, ax = plt.subplots()
sns.scatterplot(x='recency', y='monetary', hue='frequency', data=df_day, ax=ax, palette='viridis')
ax.set_title('RFM Analysis - Recency vs Monetary')
ax.set_xlabel('Recency (Days since last rental)')
ax.set_ylabel('Monetary (Total Rentals)')
st.pyplot(fig)
