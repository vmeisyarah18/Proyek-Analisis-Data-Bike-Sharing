import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# KONFIGURASI AWAL
# ==========================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

sns.set_style("whitegrid")

# ==========================
# JUDUL DASHBOARD
# ==========================
st.title("🚲 Bike Sharing Dashboard")
st.write(
    "Dashboard ini menyajikan analisis peminjaman sepeda berdasarkan "
    "kondisi cuaca, musim, waktu, dan tipe pengguna."
)

st.divider()

# LOAD DATA
df = pd.read_csv("day.csv")
df["dteday"] = pd.to_datetime(df["dteday"])

# Sidebar
st.sidebar.title("📌 Informasi")
st.sidebar.write("Dataset: Bike Sharing (day.csv)")
st.sidebar.write("Analisis dilakukan menggunakan data harian")

# PERTANYAAN BISNIS 1
st.subheader("📊 Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman")

weather_avg = df.groupby("weathersit")["cnt"].mean().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(data=weather_avg, x="weathersit", y="cnt", ax=ax1)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Rata-rata Peminjaman")
ax1.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")

st.pyplot(fig1)

st.write(
    "**Insight:** Cuaca cerah memiliki rata-rata peminjaman sepeda tertinggi. "
    "Semakin buruk kondisi cuaca, jumlah peminjaman cenderung menurun."
)

st.divider()

# PERTANYAAN BISNIS 2
st.subheader("📊 Pola Peminjaman Sepeda Berdasarkan Musim")

season_avg = df.groupby("season")["cnt"].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=season_avg, x="season", y="cnt", ax=ax2)
ax2.set_xlabel("Musim")
ax2.set_ylabel("Rata-rata Peminjaman")
ax2.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Musim")

st.pyplot(fig2)

st.write(
    "**Insight:** Musim dengan cuaca lebih nyaman menunjukkan peminjaman yang lebih tinggi, "
    "sementara musim ekstrem memiliki tingkat peminjaman yang lebih rendah."
)

st.divider()

# EDA 1: TREN WAKTU
st.subheader("📈 Tren Peminjaman Sepeda dari Waktu ke Waktu")

fig3, ax3 = plt.subplots()
ax3.plot(df["dteday"], df["cnt"])
ax3.set_xlabel("Tanggal")
ax3.set_ylabel("Jumlah Peminjaman")
ax3.set_title("Tren Harian Peminjaman Sepeda")

st.pyplot(fig3)

st.write(
    "**Insight:** Terlihat fluktuasi peminjaman sepanjang waktu dengan "
    "pola peningkatan pada periode tertentu."
)

st.divider()

# EDA 2: WEEKDAY VS WEEKEND
st.subheader("📊 Perbandingan Peminjaman Weekday vs Weekend")

weekday_avg = df.groupby("workingday")["cnt"].mean().reset_index()

fig4, ax4 = plt.subplots()
sns.barplot(data=weekday_avg, x="workingday", y="cnt", ax=ax4)
ax4.set_xticks([0, 1])
ax4.set_xticklabels(["Weekend", "Weekday"])
ax4.set_xlabel("Jenis Hari")
ax4.set_ylabel("Rata-rata Peminjaman")
ax4.set_title("Rata-rata Peminjaman: Weekday vs Weekend")

st.pyplot(fig4)

st.write(
    "**Insight:** Hari kerja memiliki rata-rata peminjaman lebih tinggi, "
    "menunjukkan sepeda sering digunakan untuk aktivitas rutin."
)

st.divider()

# EDA 3: TIPE PENGGUNA
st.subheader("👥 Komposisi Pengguna Sepeda")

user_avg = df[["casual", "registered"]].mean()

fig5, ax5 = plt.subplots()
ax5.pie(
    user_avg,
    labels=["Casual", "Registered"],
    autopct="%1.1f%%",
    startangle=90
)
ax5.set_title("Proporsi Pengguna Casual vs Registered")

st.pyplot(fig5)

st.write(
    "**Insight:** Sebagian besar peminjaman berasal dari pengguna terdaftar, "
    "menandakan tingkat loyalitas yang tinggi terhadap layanan."
)

st.divider()

# KESIMPULAN
st.subheader("📝 Kesimpulan")

st.write(
    "Berdasarkan hasil analisis, kondisi cuaca dan musim memiliki pengaruh "
    "signifikan terhadap jumlah peminjaman sepeda. Selain itu, pola penggunaan "
    "menunjukkan bahwa sepeda lebih banyak digunakan pada hari kerja oleh "
    "pengguna terdaftar, serta terdapat tren peningkatan peminjaman pada "
    "periode tertentu."
)

st.caption("📌 Sumber Data: Bike Sharing Dataset (day.csv)")
