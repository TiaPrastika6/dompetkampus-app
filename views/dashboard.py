import streamlit as st
import pandas as pd
import altair as alt

from helpers import format_rupiah
from components import metric_card


def show_dashboard():
    st.markdown(
        """
        <div class="page-heading">
            <span class="page-label">Dashboard</span>
            <h1>📊 Dashboard Keuangan</h1>
            <p>Pantau saldo, pemasukan, pengeluaran, dan kategori transaksi dalam satu halaman.</p>
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
                <p>Mulai tambahkan pemasukan atau pengeluaran di menu <b>Tambah Transaksi</b>.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    df = pd.DataFrame(data)
    df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
    df["bulan"] = df["tanggal"].dt.strftime("%Y-%m")

    daftar_bulan = sorted(df["bulan"].dropna().unique(), reverse=True)

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
            "Sisa uang setelah dikurangi pengeluaran."
        )

    st.write("")

    if saldo < 0:
        status_text = "Pengeluaran kamu lebih besar dari pemasukan. Coba cek lagi kategori yang paling banyak menghabiskan uang."
        status_class = "status-danger"
    elif saldo == 0:
        status_text = "Saldo kamu pas-pasan bulan ini. Usahakan sisakan sedikit untuk kebutuhan mendadak."
        status_class = "status-warning"
    else:
        status_text = "Saldo kamu masih aman. Pertahankan kebiasaan mencatat transaksi."
        status_class = "status-safe"

    st.markdown(
        f"""
        <div class="status-card {status_class}">
            <h3>Catatan Bulan Ini</h3>
            <p>{status_text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_grafik, col_ringkasan = st.columns([1.8, 1])

    with col_grafik:
        st.markdown("### 📌 Pengeluaran per Kategori")

        df_pengeluaran = df_filter[df_filter["jenis"] == "Pengeluaran"]

        if len(df_pengeluaran) == 0:
            st.markdown(
                """
                <div class="empty-chart">
                    <h3>Belum ada pengeluaran</h3>
                    <p>Kalau nanti kamu mencatat pengeluaran, grafik kategori akan muncul di sini.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            df_kategori = (
                df_pengeluaran
                .groupby("kategori", as_index=False)["nominal"]
                .sum()
                .sort_values(by="nominal", ascending=False)
            )

            chart = alt.Chart(df_kategori).mark_bar(
                cornerRadiusTopLeft=10,
                cornerRadiusTopRight=10,
                color="#FF9F1C"
            ).encode(
                x=alt.X("kategori:N", title=None, sort="-y"),
                y=alt.Y("nominal:Q", title="Nominal"),
                tooltip=[
                    alt.Tooltip("kategori:N", title="Kategori"),
                    alt.Tooltip("nominal:Q", title="Nominal", format=",.0f")
                ]
            ).properties(
                height=330
            ).configure_view(
                strokeWidth=0
            )

            st.altair_chart(chart, use_container_width=True)

    with col_ringkasan:
        st.markdown("### 🧾 Ringkasan")

        jumlah_transaksi = len(df_filter)
        transaksi_pemasukan = len(df_filter[df_filter["jenis"] == "Pemasukan"])
        transaksi_pengeluaran = len(df_filter[df_filter["jenis"] == "Pengeluaran"])

        st.markdown(
            f"""
            <div class="summary-list">
                <div>
                    <span>Jumlah transaksi</span>
                    <strong>{jumlah_transaksi}</strong>
                </div>
                <div>
                    <span>Transaksi pemasukan</span>
                    <strong>{transaksi_pemasukan}</strong>
                </div>
                <div>
                    <span>Transaksi pengeluaran</span>
                    <strong>{transaksi_pengeluaran}</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Transaksi Terbaru")

    df_recent = df_filter.sort_values(by="tanggal", ascending=False).head(5)

    for _, row in df_recent.iterrows():
        tanggal = row["tanggal"].strftime("%d %B %Y") if pd.notnull(row["tanggal"]) else "-"
        jenis = row["jenis"]
        kategori = row["kategori"]
        nominal = format_rupiah(row["nominal"])

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
            <div class="transaction-card compact-card">
                <div class="transaction-left">
                    <div class="transaction-icon">{icon}</div>
                    <div>
                        <h3>{kategori}</h3>
                        <p>{tanggal}</p>
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