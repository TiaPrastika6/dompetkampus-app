import streamlit as st
import pandas as pd
import altair as alt

from helpers import format_rupiah
from components import metric_card


NAMA_BULAN = {
    "01": "Januari",
    "02": "Februari",
    "03": "Maret",
    "04": "April",
    "05": "Mei",
    "06": "Juni",
    "07": "Juli",
    "08": "Agustus",
    "09": "September",
    "10": "Oktober",
    "11": "November",
    "12": "Desember",
}


def format_bulan(nilai_bulan):
    tahun, bulan = nilai_bulan.split("-")
    return f"{NAMA_BULAN[bulan]} {tahun}"


def show_dashboard():
    st.markdown(
        """
        <div class="dashboard-title-card">
            <div>
                <h1>📊 Dashboard Keuangan</h1>
                <p>Pantau pemasukan, pengeluaran, saldo, dan transaksi terbaru dalam satu halaman.</p>
            </div>
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

    st.markdown(
        """
        <div class="periode-header">
            <div>
                <h3>📅 Periode Laporan</h3>
                <p>Pilih bulan untuk melihat ringkasan keuangan.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    bulan_dipilih = st.selectbox(
        "Pilih bulan",
        daftar_bulan,
        format_func=format_bulan,
        label_visibility="collapsed"
    )

    df_filter = df[df["bulan"] == bulan_dipilih]

    total_pemasukan = df_filter[df_filter["jenis"] == "Pemasukan"]["nominal"].sum()
    total_pengeluaran = df_filter[df_filter["jenis"] == "Pengeluaran"]["nominal"].sum()
    saldo = total_pemasukan - total_pengeluaran

    st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "Total Pemasukan",
            format_rupiah(total_pemasukan),
            "💰",
            "Uang masuk bulan ini."
        )

    with col2:
        metric_card(
            "Total Pengeluaran",
            format_rupiah(total_pengeluaran),
            "🛍️",
            "Uang keluar bulan ini."
        )

    with col3:
        metric_card(
            "Saldo Akhir",
            format_rupiah(saldo),
            "✨",
            "Sisa uang bulan ini."
        )

    if saldo < 0:
        status_text = "Pengeluaran kamu lebih besar dari pemasukan. Coba cek lagi kategori yang paling banyak menghabiskan uang."
        status_class = "status-danger"
        status_icon = "⚠️"
    elif saldo == 0:
        status_text = "Saldo kamu pas-pasan bulan ini. Usahakan sisakan sedikit untuk kebutuhan mendadak."
        status_class = "status-warning"
        status_icon = "🟡"
    else:
        status_text = "Saldo kamu masih aman. Pertahankan kebiasaan mencatat transaksi."
        status_class = "status-safe"
        status_icon = "✅"

    st.markdown(
        f"""
        <div class="status-card {status_class}">
            <h3>{status_icon} Catatan Bulan Ini</h3>
            <p>{status_text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    df_pengeluaran = df_filter[df_filter["jenis"] == "Pengeluaran"]
    jumlah_transaksi = len(df_filter)
    transaksi_pemasukan = len(df_filter[df_filter["jenis"] == "Pemasukan"])
    transaksi_pengeluaran = len(df_filter[df_filter["jenis"] == "Pengeluaran"])

    col_chart, col_summary = st.columns([1.7, 1])

    with col_chart:
        st.markdown("### 📌 Pengeluaran per Kategori")

        if len(df_pengeluaran) == 0:
            st.markdown(
                """
                <div class="soft-empty-card">
                    <h3>Belum ada pengeluaran</h3>
                    <p>Kalau nanti kamu mencatat pengeluaran, grafik kategori akan muncul di bagian ini.</p>
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
                cornerRadiusTopLeft=12,
                cornerRadiusTopRight=12,
                color="#FF9F1C"
            ).encode(
                x=alt.X("kategori:N", title=None, sort="-y"),
                y=alt.Y("nominal:Q", title=None),
                tooltip=[
                    alt.Tooltip("kategori:N", title="Kategori"),
                    alt.Tooltip("nominal:Q", title="Nominal", format=",.0f")
                ]
            ).properties(
                height=280
            ).configure_view(
                strokeWidth=0
            ).configure_axis(
                labelColor="#6E4E1C",
                titleColor="#6E4E1C",
                gridColor="#F5DCA4"
            )

            st.altair_chart(chart, use_container_width=True)

    with col_summary:
        st.markdown("### 🧾 Ringkasan")

        st.markdown(
            f"""
            <div class="summary-card">
                <div class="summary-item">
                    <span>Jumlah transaksi</span>
                    <strong>{jumlah_transaksi}</strong>
                </div>
                <div class="summary-item">
                    <span>Pemasukan</span>
                    <strong>{transaksi_pemasukan}</strong>
                </div>
                <div class="summary-item">
                    <span>Pengeluaran</span>
                    <strong>{transaksi_pengeluaran}</strong>
                </div>
                <div class="summary-item last">
                    <span>Periode</span>
                    <strong>{format_bulan(bulan_dipilih)}</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 🕒 Transaksi Terbaru")

    df_recent = df_filter.sort_values(by="tanggal", ascending=False).head(5)

    for _, row in df_recent.iterrows():
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