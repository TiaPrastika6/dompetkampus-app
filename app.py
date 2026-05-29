import streamlit as st

from data_handler import load_data
from styles import load_css
from views.dashboard import show_dashboard
from views.tambah_transaksi import show_tambah_transaksi
from views.riwayat_transaksi import show_riwayat_transaksi


st.set_page_config(
    page_title="DompetKampus",
    page_icon="💸",
    layout="wide"
)

load_css()

if "data_keuangan" not in st.session_state:
    st.session_state.data_keuangan = load_data()


# =========================
# SIDEBAR
# =========================
st.sidebar.markdown("## 💛 DompetKampus")
st.sidebar.markdown("Kelola keuangan harian mahasiswa dengan lebih rapi.")

menu = st.sidebar.radio(
    "Pilih Menu",
    ["Dashboard", "Tambah Transaksi", "Riwayat Transaksi"]
)

st.sidebar.divider()
st.sidebar.markdown("### Tips Hemat")
st.sidebar.info(
    "Catat pengeluaran kecil seperti jajan, print tugas, dan parkir. "
    "Biasanya dari sana uang cepat habis."
)


# =========================
# ROUTING HALAMAN
# =========================
if menu == "Dashboard":
    st.markdown("""
    <div class="hero-card">
        <p class="hero-title">💸 DompetKampus</p>
        <p class="hero-subtitle">
            Kelola pemasukan dan pengeluaran mahasiswa dengan tampilan sederhana, hangat, dan mudah dipahami.
            Cocok untuk mencatat uang bulanan, makan, transportasi, tugas kuliah, kuota, dan kebutuhan harian.
        </p>
    </div>
    """, unsafe_allow_html=True)

    show_dashboard()

elif menu == "Tambah Transaksi":
    show_tambah_transaksi()

elif menu == "Riwayat Transaksi":
    show_riwayat_transaksi()


# =========================
# FOOTER
# =========================
st.markdown(
    '<p class="footer-note">DompetKampus — aplikasi manajemen keuangan sederhana untuk mahasiswa.</p>',
    unsafe_allow_html=True
)