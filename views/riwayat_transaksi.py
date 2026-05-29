import streamlit as st
import pandas as pd

from data_handler import save_data
from helpers import format_rupiah


def show_riwayat_transaksi():
    st.markdown('<p class="section-title">📋 Riwayat Transaksi</p>', unsafe_allow_html=True)

    data = st.session_state.data_keuangan

    if len(data) == 0:
        st.markdown(
            """
            <div class="empty-card">
                <h3>Belum ada riwayat transaksi</h3>
                <p>
                    Data pemasukan dan pengeluaran yang kamu tambahkan akan muncul di sini.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    df = pd.DataFrame(data)
    df["tanggal"] = pd.to_datetime(df["tanggal"])

    col1, col2 = st.columns(2)

    with col1:
        filter_jenis = st.selectbox(
            "Filter jenis transaksi",
            ["Semua", "Pemasukan", "Pengeluaran"]
        )

    with col2:
        filter_kategori = st.selectbox(
            "Filter kategori",
            ["Semua"] + sorted(df["kategori"].unique().tolist())
        )

    df_filter = df.copy()

    if filter_jenis != "Semua":
        df_filter = df_filter[df_filter["jenis"] == filter_jenis]

    if filter_kategori != "Semua":
        df_filter = df_filter[df_filter["kategori"] == filter_kategori]

    df_tampil = df_filter.sort_values(by="tanggal", ascending=False).copy()
    df_tampil["tanggal"] = df_tampil["tanggal"].dt.strftime("%d-%m-%Y")
    df_tampil["nominal"] = df_tampil["nominal"].apply(format_rupiah)

    st.markdown("### Data Transaksi")

    st.dataframe(
        df_tampil[["tanggal", "jenis", "kategori", "nominal", "keterangan"]],
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.markdown("### 🗑️ Hapus Transaksi")

    label_map = {}

    for item in data:
        label_map[item["id"]] = (
            f"{item['tanggal']} | {item['jenis']} | "
            f"{item['kategori']} | {format_rupiah(item['nominal'])} | "
            f"{item['keterangan']}"
        )

    id_terpilih = st.selectbox(
        "Pilih transaksi yang ingin dihapus",
        options=list(label_map.keys()),
        format_func=lambda x: label_map[x]
    )

    if st.button("Hapus Transaksi"):
        st.session_state.data_keuangan = [
            item for item in st.session_state.data_keuangan
            if item["id"] != id_terpilih
        ]

        save_data(st.session_state.data_keuangan)
        st.success("Transaksi berhasil dihapus.")
        st.rerun()