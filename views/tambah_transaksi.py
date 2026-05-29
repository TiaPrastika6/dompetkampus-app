import streamlit as st
from datetime import date, datetime

from data_handler import save_data


KATEGORI_PEMASUKAN = [
    "Uang Bulanan",
    "Beasiswa",
    "Kerja Part Time",
    "Hadiah",
    "Lainnya"
]

KATEGORI_PENGELUARAN = [
    "Makan",
    "Transportasi",
    "Tugas/Kuliah",
    "Kuota Internet",
    "Kos",
    "Hiburan",
    "Belanja",
    "Lainnya"
]


def simpan_transaksi(jenis, tanggal, kategori, nominal, keterangan):
    transaksi_baru = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
        "tanggal": str(tanggal),
        "jenis": jenis,
        "kategori": kategori,
        "nominal": int(nominal),
        "keterangan": keterangan.strip()
    }

    st.session_state.data_keuangan.append(transaksi_baru)
    save_data(st.session_state.data_keuangan)

    st.session_state.transaksi_tersimpan = True
    st.rerun()


def form_transaksi(jenis, kategori_list, form_title, form_desc, placeholder, button_label, form_key):
    with st.form(form_key, clear_on_submit=True):
        st.markdown(
            f"""
            <div class="form-clean-header">
                <h2>{form_title}</h2>
                <p>{form_desc}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            tanggal = st.date_input(
                "Tanggal transaksi",
                value=date.today(),
                key=f"tanggal_{form_key}"
            )

        with col2:
            kategori = st.selectbox(
                "Kategori transaksi",
                kategori_list,
                key=f"kategori_{form_key}"
            )

        nominal = st.number_input(
            "Nominal transaksi",
            min_value=0,
            step=1000,
            key=f"nominal_{form_key}"
        )

        keterangan = st.text_area(
            "Keterangan transaksi",
            placeholder=placeholder,
            key=f"keterangan_{form_key}"
        )

        submit = st.form_submit_button(button_label)

        if submit:
            if nominal <= 0:
                st.error("Nominal transaksi harus lebih dari 0.")
            else:
                simpan_transaksi(
                    jenis,
                    tanggal,
                    kategori,
                    nominal,
                    keterangan
                )


def show_tambah_transaksi():
    if st.session_state.pop("transaksi_tersimpan", False):
        st.toast("Transaksi berhasil disimpan.", icon="✅")

    st.markdown(
        """
        <div class="transaction-heading">
            <p class="eyebrow">DompetKampus</p>
            <h1>Tambah Transaksi</h1>
            <p>Catat pemasukan dan pengeluaran harian dengan tampilan yang lebih rapi, simpel, dan nyaman digunakan.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    tab_pengeluaran, tab_pemasukan = st.tabs([
        "🛍️ Pengeluaran",
        "💰 Pemasukan"
    ])

    with tab_pengeluaran:
        form_transaksi(
            jenis="Pengeluaran",
            kategori_list=KATEGORI_PENGELUARAN,
            form_title="Detail Pengeluaran",
            form_desc="Catat uang keluar seperti makan, transportasi, kos, kuota, atau kebutuhan kuliah.",
            placeholder="Contoh: beli makan siang, bayar print tugas, beli kuota...",
            button_label="💾 Simpan Pengeluaran",
            form_key="form_pengeluaran"
        )

    with tab_pemasukan:
        form_transaksi(
            jenis="Pemasukan",
            kategori_list=KATEGORI_PEMASUKAN,
            form_title="Detail Pemasukan",
            form_desc="Catat uang masuk seperti uang bulanan, beasiswa, hadiah, atau penghasilan tambahan.",
            placeholder="Contoh: uang bulanan dari orang tua, beasiswa, hadiah...",
            button_label="💾 Simpan Pemasukan",
            form_key="form_pemasukan"
        )