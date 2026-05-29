import streamlit as st


def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        * {
            font-family: 'Inter', sans-serif;
        }

        header[data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        .stDeployButton,
        #MainMenu,
        footer {
            display: none !important;
            visibility: hidden !important;
        }

        .stMarkdown h1 a,
        .stMarkdown h2 a,
        .stMarkdown h3 a,
        a[href^="#"] {
            display: none !important;
            visibility: hidden !important;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(255, 198, 109, 0.18), transparent 32%),
                radial-gradient(circle at top right, rgba(255, 228, 150, 0.38), transparent 30%),
                linear-gradient(135deg, #FFF9EC 0%, #FFF4DA 48%, #FFEBC2 100%);
            color: #2F1D05;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1040px;
        }

        /* =========================
           SIDEBAR
        ========================= */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FFF3D3 0%, #FFE4A6 100%);
            border-right: 1px solid rgba(180, 105, 20, 0.12);
        }

        section[data-testid="stSidebar"] * {
            color: #3A2607;
        }

        section[data-testid="stSidebar"] .stRadio {
            background: rgba(255, 255, 255, 0.62);
            border: 1px solid rgba(255, 184, 77, 0.28);
            border-radius: 22px;
            padding: 16px 18px 10px 18px;
            box-shadow: 0 12px 28px rgba(181, 111, 32, 0.07);
        }

        section[data-testid="stSidebar"] .stRadio label {
            font-size: 15px !important;
            font-weight: 650 !important;
        }

        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            line-height: 1.55;
        }

        /* =========================
           HERO DASHBOARD
        ========================= */
        .hero-card {
            background:
                radial-gradient(circle at top right, rgba(255,255,255,0.55), transparent 30%),
                linear-gradient(135deg, #FFB13B 0%, #FFD166 55%, #FFE9A6 100%);
            padding: 30px 38px;
            border-radius: 30px;
            box-shadow: 0 22px 50px rgba(195, 112, 21, 0.18);
            margin-bottom: 28px;
            border: 1px solid rgba(255, 255, 255, 0.75);
        }

        .hero-title {
            font-size: 42px;
            font-weight: 850;
            margin: 0;
            color: #382206;
            letter-spacing: -1px;
        }

        .hero-subtitle {
            font-size: 16px;
            margin-top: 10px;
            margin-bottom: 0;
            color: #5C4218;
            max-width: 820px;
            line-height: 1.75;
            font-weight: 500;
        }

        /* =========================
           HALAMAN TAMBAH TRANSAKSI
        ========================= */
        .transaction-heading {
            padding-top: 6px;
            margin-bottom: 26px;
        }

        .transaction-heading .eyebrow {
            display: inline-flex;
            align-items: center;
            width: fit-content;
            padding: 7px 14px;
            border-radius: 999px;
            background: rgba(255, 177, 59, 0.18);
            border: 1px solid rgba(255, 177, 59, 0.35);
            color: #B85C00;
            font-size: 13px;
            font-weight: 800;
            margin: 0 0 14px 0;
        }

        .transaction-heading h1 {
            font-size: 42px;
            font-weight: 850;
            color: #2F1D05;
            margin: 0 0 12px 0;
            letter-spacing: -1px;
            line-height: 1.1;
        }

        .transaction-heading p {
            color: #75521A;
            font-size: 16px;
            line-height: 1.75;
            margin: 0;
            max-width: 720px;
        }

        /* =========================
           TAB TRANSAKSI
        ========================= */
        div[data-testid="stTabs"] {
            background: rgba(255, 255, 255, 0.62);
            border: 1px solid rgba(255, 184, 77, 0.28);
            border-radius: 30px;
            padding: 20px 22px 26px 22px;
            box-shadow: 0 20px 45px rgba(164, 97, 19, 0.10);
            margin-top: 12px;
        }

        div[data-testid="stTabs"] [role="tablist"] {
            display: grid !important;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 22px;
        }

        div[data-testid="stTabs"] button[data-baseweb="tab"] {
            width: 100%;
            height: 58px;
            border-radius: 18px;
            background: rgba(255, 253, 248, 0.88);
            border: 1.5px solid rgba(255, 173, 72, 0.42);
            box-shadow: 0 10px 22px rgba(180, 105, 20, 0.06);
            color: #4B3109;
            font-weight: 850;
            justify-content: center;
        }

        div[data-testid="stTabs"] button[data-baseweb="tab"] p {
            color: #4B3109 !important;
            font-weight: 850 !important;
            font-size: 15px !important;
        }

        div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(135deg, #FFB13B, #FF9F1C);
            border-color: rgba(255, 159, 28, 0.85);
            box-shadow: 0 14px 28px rgba(255, 159, 28, 0.26);
        }

        div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] p {
            color: #2F1D05 !important;
        }

        div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
            display: none !important;
        }

        /* =========================
           FORM TRANSAKSI
        ========================= */
        div[data-testid="stForm"] {
            background:
                radial-gradient(circle at top right, rgba(255, 209, 102, 0.13), transparent 35%),
                rgba(255, 255, 255, 0.95);
            padding: 34px 38px;
            border-radius: 26px;
            box-shadow: 0 24px 58px rgba(164, 97, 19, 0.13);
            border: 1px solid rgba(255, 181, 77, 0.32);
            margin-top: 6px;
            margin-bottom: 6px;
        }

        .form-clean-header {
            padding-bottom: 22px;
            margin-bottom: 24px;
            border-bottom: 1px solid rgba(128, 89, 28, 0.12);
        }

        .form-clean-header h2 {
            margin: 0 0 8px 0;
            color: #2F1D05;
            font-size: 26px;
            font-weight: 850;
            letter-spacing: -0.5px;
        }

        .form-clean-header p {
            margin: 0;
            color: #75521A;
            font-size: 15px;
            line-height: 1.6;
            max-width: 760px;
        }

        .page-heading {
            display: block !important;
            margin-bottom: 26px;
            padding-top: 4px;
        }

        .page-heading h1 {
            font-size: 40px;
            font-weight: 850;
            color: #2F1D05;
            margin: 0 0 12px 0;
            letter-spacing: -0.9px;
            line-height: 1.15;
        }

        .page-heading p {
            color: #75521A;
            font-size: 16px;
            line-height: 1.7;
            margin: 0;
            max-width: 760px;
        }

        .page-label {
            display: none !important;
        }

        .section-title {
            font-size: 32px;
            font-weight: 850;
            color: #2F1D05;
            margin-bottom: 20px;
            letter-spacing: -0.6px;
        }

        /* =========================
           INPUT
        ========================= */
        label,
        .stRadio label,
        .stSelectbox label,
        .stDateInput label,
        .stNumberInput label,
        .stTextArea label {
            color: #4B3109 !important;
            font-weight: 750 !important;
            font-size: 15px !important;
        }

        div[data-baseweb="select"] > div,
        div[data-testid="stTextInput"] input,
        div[data-testid="stNumberInput"] input,
        div[data-testid="stDateInput"] input,
        textarea {
            background-color: #FFFDF8 !important;
            color: #2F1D05 !important;
            border-radius: 16px !important;
            border: 1.5px solid rgba(255, 173, 72, 0.48) !important;
            box-shadow: 0 8px 20px rgba(180, 105, 20, 0.045) !important;
        }

        div[data-baseweb="select"] > div {
            min-height: 54px !important;
        }

        div[data-testid="stTextInput"] input,
        div[data-testid="stNumberInput"] input,
        div[data-testid="stDateInput"] input {
            min-height: 54px !important;
        }

        textarea {
            min-height: 110px !important;
        }

        div[data-baseweb="select"] > div:hover,
        div[data-testid="stTextInput"] input:hover,
        div[data-testid="stNumberInput"] input:hover,
        div[data-testid="stDateInput"] input:hover,
        textarea:hover {
            border-color: rgba(255, 159, 28, 0.9) !important;
        }

        div[data-baseweb="select"] span {
            color: #2F1D05 !important;
            font-weight: 650 !important;
        }

        input::placeholder,
        textarea::placeholder {
            color: #A98243 !important;
        }

        /* =========================
           BUTTON
        ========================= */
        .stButton > button,
        .stFormSubmitButton > button {
            background: linear-gradient(135deg, #FFB13B, #FF9F1C);
            color: #2F1D05;
            border: none;
            border-radius: 16px;
            padding: 0.85rem 1.45rem;
            font-weight: 850;
            font-size: 16px;
            box-shadow: 0 14px 28px rgba(255, 159, 28, 0.28);
            transition: all 0.2s ease;
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 35px rgba(255, 159, 28, 0.36);
            color: #2F1D05;
            border: none;
        }

        .stFormSubmitButton > button {
            min-width: 220px;
            height: 56px;
        }

        /* =========================
           DASHBOARD
        ========================= */
        .dashboard-title-card {
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid rgba(255, 190, 104, 0.35);
            border-radius: 28px;
            padding: 28px 32px;
            margin-bottom: 22px;
            box-shadow: 0 18px 38px rgba(181, 111, 32, 0.10);
        }

        .dashboard-title-card h1 {
            font-size: 36px;
            font-weight: 850;
            color: #2F1D05;
            margin: 0 0 8px 0;
            letter-spacing: -0.8px;
        }

        .dashboard-title-card p {
            color: #75521A;
            font-size: 16px;
            line-height: 1.65;
            margin: 0;
        }

        .periode-header {
            background: linear-gradient(135deg, rgba(255,255,255,0.86), rgba(255,241,199,0.78));
            border: 1px solid rgba(255, 190, 104, 0.38);
            border-radius: 24px 24px 8px 8px;
            padding: 18px 24px;
            box-shadow: 0 12px 26px rgba(181, 111, 32, 0.08);
        }

        .periode-header h3 {
            margin: 0 0 4px 0;
            color: #2F1D05;
            font-size: 19px;
            font-weight: 850;
        }

        .periode-header p {
            margin: 0;
            color: #7A5519;
            font-size: 14px;
        }

        .section-gap {
            height: 18px;
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.86);
            backdrop-filter: blur(10px);
            padding: 24px;
            border-radius: 26px;
            box-shadow: 0 18px 38px rgba(181, 111, 32, 0.12);
            border: 1px solid rgba(255, 190, 104, 0.36);
            min-height: 145px;
        }

        .metric-top {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .metric-icon {
            width: 56px;
            height: 56px;
            border-radius: 18px;
            background: linear-gradient(135deg, #FFE8A3, #FFB84D);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            box-shadow: inset 0 0 0 1px rgba(255,255,255,0.6);
        }

        .metric-title {
            margin: 0;
            color: #80591C;
            font-size: 14px;
            font-weight: 800;
        }

        .metric-value {
            margin: 5px 0 0 0;
            color: #2F1D05;
            font-size: 26px;
            font-weight: 850;
            letter-spacing: -0.4px;
        }

        .metric-note {
            margin-top: 16px;
            margin-bottom: 0;
            color: #7A5519;
            font-size: 13px;
            line-height: 1.5;
        }

        .status-card {
            padding: 22px 26px;
            border-radius: 24px;
            margin: 24px 0 28px 0;
            box-shadow: 0 14px 30px rgba(181, 111, 32, 0.10);
        }

        .status-card h3 {
            margin: 0 0 8px 0;
            font-size: 20px;
            font-weight: 850;
        }

        .status-card p {
            margin: 0;
            line-height: 1.6;
            font-size: 15px;
        }

        .status-safe {
            background: linear-gradient(135deg, #EAF7DF, #F6FFE9);
            border: 1px solid #CBE9B8;
            color: #2E7D32;
        }

        .status-warning {
            background: linear-gradient(135deg, #FFF3CD, #FFF8E1);
            border: 1px solid #FFE08A;
            color: #8A5A00;
        }

        .status-danger {
            background: linear-gradient(135deg, #FFE1DC, #FFF2EF);
            border: 1px solid #FFB9AD;
            color: #A23A2A;
        }

        .empty-card,
        .content-card {
            background: rgba(255, 255, 255, 0.84);
            padding: 28px;
            border-radius: 28px;
            box-shadow: 0 18px 40px rgba(181, 111, 32, 0.12);
            border: 1px solid rgba(255, 190, 104, 0.35);
            margin-bottom: 22px;
        }

        .empty-card h3 {
            color: #3B2506;
            margin-bottom: 10px;
        }

        .empty-card p {
            color: #6E4E1C;
            font-size: 16px;
            line-height: 1.6;
        }

        .soft-empty-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.78), rgba(255,241,199,0.72));
            border: 1px dashed rgba(255, 159, 28, 0.45);
            border-radius: 24px;
            padding: 30px;
            min-height: 210px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 14px 30px rgba(181, 111, 32, 0.08);
        }

        .soft-empty-card h3 {
            margin: 0 0 10px 0;
            color: #2F1D05;
            font-size: 22px;
            font-weight: 850;
        }

        .soft-empty-card p {
            margin: 0;
            color: #75521A;
            font-size: 15px;
            line-height: 1.6;
        }

        .filter-title {
            font-size: 18px;
            font-weight: 800;
            color: #3A2607;
            margin-bottom: 10px;
        }

        .mini-stat-card {
            background: rgba(255, 255, 255, 0.84);
            border: 1px solid rgba(255, 190, 104, 0.35);
            border-radius: 22px;
            padding: 20px 24px;
            box-shadow: 0 14px 30px rgba(181, 111, 32, 0.10);
            margin: 18px 0 22px 0;
        }

        .mini-stat-card p {
            margin: 0;
            color: #80591C;
            font-size: 14px;
            font-weight: 700;
        }

        .mini-stat-card h3 {
            margin: 8px 0 0 0;
            color: #2F1D05;
            font-size: 26px;
            font-weight: 850;
        }

        .transaction-card {
            background: rgba(255, 255, 255, 0.88);
            border: 1px solid rgba(255, 190, 104, 0.35);
            border-radius: 24px;
            padding: 18px 22px;
            margin: 12px 0;
            box-shadow: 0 16px 35px rgba(181, 111, 32, 0.10);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
        }

        .transaction-left {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .transaction-icon {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #FFF1B8, #FFC46B);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 23px;
            flex-shrink: 0;
        }

        .transaction-left h3,
        .transaction-right h3 {
            margin: 0;
            font-size: 17px;
            font-weight: 850;
            color: #2F1D05;
        }

        .transaction-left p {
            margin: 5px 0 0 0;
            color: #7B5A22;
            font-size: 13px;
        }

        .transaction-right {
            text-align: right;
            min-width: 120px;
        }

        .transaction-badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 800;
            margin-bottom: 7px;
        }

        .badge-income {
            background: #E9F8DF;
            color: #2E7D32;
        }

        .badge-expense {
            background: #FFE6D6;
            color: #B45309;
        }

        .amount-income {
            color: #2E7D32 !important;
        }

        .amount-expense {
            color: #B45309 !important;
        }

        .summary-card {
            background: rgba(255, 255, 255, 0.84);
            border: 1px solid rgba(255, 190, 104, 0.36);
            border-radius: 24px;
            padding: 20px 22px;
            box-shadow: 0 16px 35px rgba(181, 111, 32, 0.10);
        }

        .summary-item {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            padding: 13px 0;
            border-bottom: 1px solid rgba(128, 89, 28, 0.12);
        }

        .summary-item.last {
            border-bottom: none;
        }

        .summary-item span {
            color: #75521A;
            font-size: 14px;
            font-weight: 600;
        }

        .summary-item strong {
            color: #2F1D05;
            font-size: 15px;
            font-weight: 850;
        }

        .summary-list {
            background: rgba(255, 255, 255, 0.84);
            border: 1px solid rgba(255, 190, 104, 0.35);
            border-radius: 24px;
            padding: 20px;
            box-shadow: 0 14px 30px rgba(181, 111, 32, 0.10);
        }

        .summary-list div {
            display: flex;
            justify-content: space-between;
            padding: 13px 0;
            border-bottom: 1px solid rgba(128, 89, 28, 0.12);
        }

        .summary-list div:last-child {
            border-bottom: none;
        }

        .summary-list span {
            color: #75521A;
            font-size: 14px;
        }

        .summary-list strong {
            color: #2F1D05;
            font-size: 16px;
        }

        div[data-testid="stDataFrame"] {
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 14px 30px rgba(181, 111, 32, 0.08);
        }

        .footer-note {
            text-align: center;
            color: #8B6A2D;
            font-size: 13px;
            margin-top: 42px;
        }

        @media screen and (max-width: 768px) {
            .hero-title {
                font-size: 32px;
            }

            .hero-card {
                padding: 24px;
            }

            .transaction-heading h1,
            .page-heading h1,
            .dashboard-title-card h1 {
                font-size: 30px;
            }

            div[data-testid="stTabs"] [role="tablist"] {
                grid-template-columns: 1fr;
            }

            div[data-testid="stForm"] {
                padding: 26px;
            }

            .transaction-card {
                flex-direction: column;
                align-items: flex-start;
            }

            .transaction-right {
                text-align: left;
                min-width: auto;
            }
        }
    </style>
    """, unsafe_allow_html=True)