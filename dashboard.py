import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")


# Membaca data dari file CSV
data1 = pd.read_csv('hour.csv')
data2 = pd.read_csv('day.csv')

# Judul Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")
st.write("""Analisis ini bertujuan untuk memahami pola penyewaan sepeda berdasarkan data yang tersedia. 
Dengan menganalisis data penyewaan sepeda, kita dapat mengidentifikasi tren dan pola yang 
dapat membantu dalam pengambilan keputusan terkait pengelolaan penyewaan sepeda. 
Data yang digunakan mencakup penyewaan per jam dan per hari, yang memungkinkan kita untuk melihat variasi penyewaan berdasarkan waktu.""")

# Pilihan untuk selectbox
options = ["Informasi Dataset","Deskripsi Data"]
selected_option = st.selectbox("Select:", options)
if st.button("Show"):
    if selected_option == "Informasi Dataset":
        st.subheader("Dataset Per Jam")
        st.write(data1)
        st.subheader("Dataset Per Hari")
        st.write(data2)

    elif selected_option == "Deskripsi Data":
        st.subheader("Deskripsi Dataset Per Jam")
        st.write(data1.describe())
        st.subheader("Deskripsi Dataset Per Hari")
        st.write(data2.describe())


# Menambahkan analisis lanjutan
# Pilihan untuk selectbox
options = ["Rata-rata Penyewaan per Jam","Rata-rata Penyewaan per Hari","Rata-rata Penyewaan per Bulan", "Rata-rata Penyewaan per Musim", "Distribusi Jumlah Penyewaan"]
selected_option = st.selectbox("Pilih Visualisasi Analisis Lanjutan:", options)

# Visualisasi Rata-rata Penyewaan per Jam
if st.button("Tampilkan"):
    if selected_option == "Rata-rata Penyewaan per Jam":
        st.subheader("Rata-rata Penyewaan per Jam")
        st.write("""Pada visualisasi ini, kita dapat melihat grafik yang menampilkan rata-rata penyewaan sepeda per jam """)
        rata_rata_penyewaan_per_jam = data1.groupby('hr')['cnt'].mean()
        fig, ax = plt.subplots()
        rata_rata_penyewaan_per_jam.plot(kind='bar', color='red', edgecolor='black', ax=ax)
        ax.set_title('Rata-rata Penyewaan per Jam')
        ax.set_xlabel('Jam')
        ax.set_ylabel('Rata-rata Penyewaan')
        st.pyplot(fig)

# Visualisasi Rata-rata Penyewaan per Hari
    elif selected_option == "Rata-rata Penyewaan per Hari":
        st.subheader("Rata-rata Penyewaan per Hari")
        st.write("""Pada visualisasi ini, kita dapat melihat grafik yang menampilkan rata-rata penyewaan sepeda per hari """)
        rata_rata_penyewaan_per_hari = data1.groupby('weekday')['cnt'].mean()
        fig, ax = plt.subplots()
        rata_rata_penyewaan_per_hari.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
        ax.set_title('Rata-rata Penyewaan per Hari')
        ax.set_xticks(ticks=np.arange(7), labels=['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'], fontweight='bold', rotation=0)
        ax.set_ylabel('Rata-rata Penyewaan')
        st.pyplot(fig)

# Rata-rata penyewaan berdasarkan bulan
    elif selected_option == "Rata-rata Penyewaan per Bulan":
        st.subheader("Rata-rata Penyewaan per Bulan")
        st.write("""Pada visualisasi ini, kita dapat melihat grafik yang menampilkan rata-rata penyewaan sepeda per bulan""")
        rata_rata_penyewaan_per_bulan_data2 = data2.groupby('mnth')['cnt'].mean()
        fig, ax = plt.subplots()
        rata_rata_penyewaan_per_bulan_data2.plot(kind='bar', color='red', edgecolor='black')
        ax.set_title('RATA-RATA PENYEWAAN PER BULAN (Data 2)', fontweight='bold')
        ax.set_xlabel('Bulan', fontweight='bold')
        ax.set_ylabel('Rata-rata Penyewaan', fontweight='bold')
        ax.set_xticks(ticks=np.arange(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'], fontweight='bold', rotation=0)
        st.pyplot(fig)

#Rata-rata penyewaan per Musim
    elif selected_option == "Rata-rata Penyewaan per Musim":
        st.subheader("Rata-rata Penyewaan per Musim")
        st.write("""Pada visualisasi ini, kita dapat melihat grafik yang menampilkan rata-rata penyewaan sepeda per Musim """)
        rata_rata_penyewaan_per_musim = data2.groupby('season')['cnt'].mean()
        fig, ax = plt.subplots()
        rata_rata_penyewaan_per_musim.plot(kind='bar', color='green', edgecolor='black', ax=ax)
        ax.set_title('Rata-rata Penyewaan per Musim')
        ax.set_xlabel('Musim', fontweight='bold')
        ax.set_ylabel('Rata-rata Penyewaan', fontweight='bold')
        ax.set_xticks(ticks=np.arange(4), labels=['Semi', 'Panas', 'Gugur', 'Dingin'], fontweight='bold', rotation=0)
        st.pyplot(fig)

# Visualisasi frekuensi jumlah penyewaan
    elif selected_option == "Distribusi Jumlah Penyewaan":
        st.subheader("Distribusi jumlah penyewaan")
        st.write("""Pada visualisasi ini, grafik akan menampilkan distribusi yang diberikan berdasarkan jumlah penyewaan""")
        fig, ax = plt.subplots()
        ax.hist(data1['cnt'], bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
        ax.set_title('DISTRIBUSI JUMLAH PENYEWAAN', fontweight='bold')
        ax.set_xlabel('Jumlah Penyewaan', fontweight='bold')
        ax.set_ylabel('Frekuensi', fontweight='bold')
        st.pyplot(fig)
