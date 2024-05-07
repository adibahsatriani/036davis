import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Membaca data dari file tips.csv
data = pd.read_csv("tips.csv")

st.title('Visualisasi Data Tip Restoran')

#Visualisasi distribusi nilai tip
st.subheader('Distribusi Nilai Tip')
fig, ax = plt.subplots()
sns.histplot(data['tip'], bins=20, color='skyblue', edgecolor='black')
ax.set_xlabel('Nilai Tip ($)')
ax.set_ylabel('Jumlah Order')
st.pyplot(fig)

#Visualisasi distribusi ukuran kelompok pelanggan
st.subheader('Distribusi Ukuran Kelompok Pelanggan')
size_counts = data['size'].value_counts()
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(size_counts.index, size_counts.values, color='lightgreen', edgecolor='black')
ax.set_xlabel('Ukuran Kelompok')
ax.set_ylabel('Jumlah Order')
st.pyplot(fig)

#Visualisasi rata-rata tip berdasarkan ukuran kelompok
st.subheader('Rata-rata Tip Berdasarkan Ukuran Kelompok')
average_tip_by_size = data.groupby('size')['tip'].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='size', y='tip', data=average_tip_by_size, palette='viridis')
ax.set_xlabel('Ukuran Kelompok')
ax.set_ylabel('Rata-rata Tip ($)')
st.pyplot(fig)