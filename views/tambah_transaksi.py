import streamlit as st
from datetime import date, datetime

from data_handler import save_data


def show_tambah_transaksi():
    st.markdown(
        """
        <div class="page-heading">
            <div>
                <p class="page-label">Form Transaksi</p>
                <h1>➕ Tambah Transaksi</h1>
                <p>Catat pemasukan dan pengeluaran harian agar keuangan mahasiswa lebih terkontrol.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    jenis = st.radio(
        "Pilih jenis transaksi",
        ["Pemasukan", "Pengeluaran"],
        horizontal=True,
        key="jenis_transaksi"
    )

    if jenis == "Pemasukan":
        st.markdown(
            """
            <div class="info-card income-card">
                <h3>💰 Pemasukan</h3>
                <p>Gunakan bagian ini untuk mencatat uang bulanan, beasiswa, hadiah, atau penghasilan tambahan.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="info-card expense-card">
                <h3>🛍️ Pengeluaran</h3>
                <p>Gunakan bagian ini untuk mencatat kebutuhan harian seperti makan, transportasi, kuota, kos, dan tugas kuliah.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.form("form_transaksi"):
        st.markdown('<p class="form-title">Detail Transaksi</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            tanggal = st.date_input(
                "Tanggal transaksi",
                value=date.today()
            )

        with col2:
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
            step=1000,
            placeholder="Masukkan nominal transaksi"
        )

        keterangan = st.text_area(
            "Keterangan",
            placeholder="Contoh: beli makan siang, bayar print tugas, uang bulanan dari orang tua..."
        )

        st.markdown('<div class="button-space"></div>', unsafe_allow_html=True)

        submit = st.form_submit_button("💾 Simpan Transaksi")

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