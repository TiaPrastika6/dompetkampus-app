import streamlit as st
import pandas as pd
import altair as alt

from helpers import format_rupiah
from components import metric_card


def show_dashboard():
    st.markdown('<p class="section-title">📊 Dashboard Keuangan</p>', unsafe_allow_html=True)

    data = st.session_state.data_keuangan

    if len(data) == 0:
        st.markdown(
            """
            <div class="empty-card">
                <h3>Belum ada transaksi</h3>
                <p>
                    Mulai tambahkan pemasukan atau pengeluaran di menu
                    <b>Tambah Transaksi</b>.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    df = pd.DataFrame(data)
    df["tanggal"] = pd.to_datetime(df["tanggal"])
    df["bulan"] = df["tanggal"].dt.strftime("%Y-%m")

    daftar_bulan = sorted(df["bulan"].unique(), reverse=True)

    bulan_dipilih = st.selectbox(
        "Pilih bulan",
        daftar_bulan
    )

    df_filter = df[df["bulan"] == bulan_dipilih]

    total_pemasukan = df_filter[df_filter["jenis"] == "Pemasukan"]["nominal"].sum()
    total_pengeluaran = df_filter[df_filter["jenis"] == "Pengeluaran"]["nominal"].sum()
    saldo = total_pemasukan - total_pengeluaran

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "Total Pemasukan",
            format_rupiah(total_pemasukan),
            "💰",
            "Jumlah uang masuk pada bulan yang dipilih."
        )

    with col2:
        metric_card(
            "Total Pengeluaran",
            format_rupiah(total_pengeluaran),
            "🛍️",
            "Jumlah uang keluar untuk kebutuhan mahasiswa."
        )

    with col3:
        metric_card(
            "Saldo Akhir",
            format_rupiah(saldo),
            "✨",
            "Sisa uang dari pemasukan dikurangi pengeluaran."
        )

    st.write("")

    col_grafik, col_ringkasan = st.columns([2, 1])

    with col_grafik:
        st.markdown("### 📌 Pengeluaran per Kategori")

        df_pengeluaran = df_filter[df_filter["jenis"] == "Pengeluaran"]

        if len(df_pengeluaran) == 0:
            st.warning("Belum ada data pengeluaran pada bulan ini.")
        else:
            df_kategori = (
                df_pengeluaran
                .groupby("kategori", as_index=False)["nominal"]
                .sum()
                .sort_values(by="nominal", ascending=False)
            )

            chart = alt.Chart(df_kategori).mark_bar(
                cornerRadiusTopLeft=8,
                cornerRadiusTopRight=8,
                color="#FFB84D"
            ).encode(
                x=alt.X("kategori:N", title="Kategori", sort="-y"),
                y=alt.Y("nominal:Q", title="Nominal"),
                tooltip=[
                    alt.Tooltip("kategori:N", title="Kategori"),
                    alt.Tooltip("nominal:Q", title="Nominal", format=",.0f")
                ]
            ).properties(
                height=360
            )

            st.altair_chart(chart, use_container_width=True)

    with col_ringkasan:
        st.markdown("### 🧾 Ringkasan Bulan Ini")

        jumlah_transaksi = len(df_filter)
        transaksi_pemasukan = len(df_filter[df_filter["jenis"] == "Pemasukan"])
        transaksi_pengeluaran = len(df_filter[df_filter["jenis"] == "Pengeluaran"])

        st.write(f"Jumlah transaksi: **{jumlah_transaksi}**")
        st.write(f"Transaksi pemasukan: **{transaksi_pemasukan}**")
        st.write(f"Transaksi pengeluaran: **{transaksi_pengeluaran}**")

        if saldo < 0:
            st.error("Pengeluaran kamu lebih besar dari pemasukan.")
        elif saldo == 0:
            st.warning("Saldo kamu pas-pasan bulan ini.")
        else:
            st.success("Saldo kamu masih aman.")