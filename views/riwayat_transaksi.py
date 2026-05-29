import streamlit as st
import pandas as pd

from data_handler import save_data
from helpers import format_rupiah


def show_riwayat_transaksi():
    if st.session_state.pop("hapus_berhasil", False):
        st.toast("Transaksi berhasil dihapus.", icon="🗑️")

    st.markdown(
        """
        <div class="page-heading">
            <h1>📋 Riwayat Transaksi</h1>
            <p>Lihat, filter, dan hapus transaksi pemasukan maupun pengeluaran yang sudah dicatat.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    data = st.session_state.data_keuangan

    if len(data) == 0:
        st.markdown(
            """
            <div class="empty-card">
                <h3>Belum ada transaksi</h3>
                <p>Data pemasukan dan pengeluaran yang kamu tambahkan akan muncul di sini.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    df = pd.DataFrame(data)
    df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")

    st.markdown('<div class="filter-title">Filter Transaksi</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        filter_jenis = st.selectbox(
            "Filter jenis transaksi",
            ["Semua", "Pemasukan", "Pengeluaran"]
        )

    with col2:
        filter_kategori = st.selectbox(
            "Filter kategori",
            ["Semua"] + sorted(df["kategori"].dropna().unique().tolist())
        )

    df_filter = df.copy()

    if filter_jenis != "Semua":
        df_filter = df_filter[df_filter["jenis"] == filter_jenis]

    if filter_kategori != "Semua":
        df_filter = df_filter[df_filter["kategori"] == filter_kategori]

    total_nominal = df_filter["nominal"].sum()
    jumlah_transaksi = len(df_filter)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown(
            f"""
            <div class="mini-stat-card">
                <p>Total Transaksi</p>
                <h3>{jumlah_transaksi}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(
            f"""
            <div class="mini-stat-card">
                <p>Total Nominal Terfilter</p>
                <h3>{format_rupiah(total_nominal)}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Daftar Transaksi")

    if len(df_filter) == 0:
        st.warning("Tidak ada transaksi yang sesuai dengan filter.")
        return

    df_filter = df_filter.sort_values(by="tanggal", ascending=False)

    for _, row in df_filter.iterrows():
        id_transaksi = row["id"]
        tanggal = row["tanggal"].strftime("%d %B %Y") if pd.notnull(row["tanggal"]) else "-"
        jenis = row["jenis"]
        kategori = row["kategori"]
        nominal = format_rupiah(row["nominal"])
        keterangan = row["keterangan"] if row["keterangan"] else "Tidak ada keterangan"

        if jenis == "Pemasukan":
            badge_class = "badge-income"
            amount_class = "amount-income"
            icon = "💰"
        else:
            badge_class = "badge-expense"
            amount_class = "amount-expense"
            icon = "🛍️"

        st.markdown(
            f"""
            <div class="transaction-card">
                <div class="transaction-left">
                    <div class="transaction-icon">{icon}</div>
                    <div>
                        <h3>{kategori}</h3>
                        <p>{tanggal} • {keterangan}</p>
                    </div>
                </div>
                <div class="transaction-right">
                    <span class="transaction-badge {badge_class}">{jenis}</span>
                    <h3 class="{amount_class}">{nominal}</h3>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col_empty, col_delete = st.columns([5, 1])

        with col_delete:
            if st.button("Hapus", key=f"hapus_{id_transaksi}"):
                st.session_state.data_keuangan = [
                    item for item in st.session_state.data_keuangan
                    if item["id"] != id_transaksi
                ]

                save_data(st.session_state.data_keuangan)
                st.session_state.hapus_berhasil = True
                st.rerun()