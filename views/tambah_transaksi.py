import streamlit as st
from datetime import date, datetime

from data_handler import save_data


def show_tambah_transaksi():
    st.markdown('<p class="section-title">➕ Tambah Transaksi</p>', unsafe_allow_html=True)

    # Jenis transaksi ditaruh DI LUAR form
    jenis = st.radio(
        "Jenis transaksi",
        ["Pemasukan", "Pengeluaran"],
        horizontal=True,
        key="jenis_transaksi"
    )

    with st.form("form_transaksi"):
        tanggal = st.date_input(
            "Tanggal transaksi",
            value=date.today()
        )

        if jenis == "Pemasukan":
            kategori = st.selectbox(
                "Kategori pemasukan",
                ["Uang Bulanan", "Beasiswa", "Kerja Part Time", "Hadiah", "Lainnya"],
                key="kategori_pemasukan"
            )
        else:
            kategori = st.selectbox(
                "Kategori pengeluaran",
                [
                    "Makan",
                    "Transportasi",
                    "Tugas/Kuliah",
                    "Kuota Internet",
                    "Kos",
                    "Hiburan",
                    "Belanja",
                    "Lainnya"
                ],
                key="kategori_pengeluaran"
            )

        nominal = st.number_input(
            "Nominal",
            min_value=0,
            step=1000
        )

        keterangan = st.text_area(
            "Keterangan",
            placeholder="Contoh: beli makan siang, bayar print tugas, uang bulanan dari orang tua..."
        )

        submit = st.form_submit_button("Simpan Transaksi")

        if submit:
            if nominal <= 0:
                st.error("Nominal harus lebih dari 0.")
            else:
                transaksi_baru = {
                    "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
                    "tanggal": str(tanggal),
                    "jenis": jenis,
                    "kategori": kategori,
                    "nominal": int(nominal),
                    "keterangan": keterangan
                }

                st.session_state.data_keuangan.append(transaksi_baru)
                save_data(st.session_state.data_keuangan)

                st.success("Transaksi berhasil disimpan.")