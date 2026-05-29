import streamlit as st


def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        * {
            font-family: 'Inter', sans-serif;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        .stDeployButton,
        #MainMenu,
        footer {
            display: none !important;
            visibility: hidden !important;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(255, 196, 107, 0.45), transparent 32%),
                radial-gradient(circle at top right, rgba(255, 232, 163, 0.55), transparent 28%),
                linear-gradient(135deg, #FFF9EC 0%, #FFF3D6 45%, #FFE7B0 100%);
            color: #332006;
        }

        .block-container {
            padding-top: 1.4rem;
            padding-bottom: 3rem;
            max-width: 1180px;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FFF2CC 0%, #FFE4A6 100%);
            border-right: 1px solid rgba(180, 105, 20, 0.12);
        }

        section[data-testid="stSidebar"] * {
            color: #3A2607;
        }

        section[data-testid="stSidebar"] .stRadio label {
            font-size: 15px !important;
            font-weight: 600 !important;
        }

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

        .page-heading {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 6px;
            margin-bottom: 20px;
        }

        .page-heading h1 {
            font-size: 34px;
            font-weight: 850;
            color: #2F1D05;
            margin: 0;
            letter-spacing: -0.7px;
        }

        .page-heading p {
            margin: 8px 0 0 0;
            color: #7A5519;
            font-size: 15px;
            line-height: 1.6;
        }

        .page-label {
            display: inline-block;
            background: rgba(255, 159, 28, 0.16);
            color: #B85C00 !important;
            padding: 7px 13px;
            border-radius: 999px;
            font-size: 13px !important;
            font-weight: 800;
            margin-bottom: 8px !important;
            border: 1px solid rgba(255, 159, 28, 0.24);
        }

        .section-title {
            font-size: 30px;
            font-weight: 850;
            color: #2F1D05;
            margin-bottom: 20px;
            letter-spacing: -0.6px;
        }

        .info-card {
            padding: 20px 24px;
            border-radius: 24px;
            margin-bottom: 18px;
            box-shadow: 0 16px 35px rgba(181, 111, 32, 0.10);
            border: 1px solid rgba(255, 190, 104, 0.45);
        }

        .info-card h3 {
            margin: 0 0 6px 0;
            font-size: 21px;
            color: #2F1D05;
        }

        .info-card p {
            margin: 0;
            color: #70501B;
            line-height: 1.65;
            font-size: 15px;
        }

        .income-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.85), rgba(255,239,187,0.88));
        }

        .expense-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.86), rgba(255,226,174,0.9));
        }

        div[data-testid="stForm"] {
            background:
                radial-gradient(circle at top right, rgba(255, 209, 102, 0.28), transparent 28%),
                rgba(255, 255, 255, 0.82);
            padding: 34px;
            border-radius: 32px;
            box-shadow: 0 24px 55px rgba(164, 97, 19, 0.14);
            border: 1px solid rgba(255, 181, 77, 0.38);
            margin-top: 8px;
        }

        .form-title {
            font-size: 22px;
            font-weight: 850;
            color: #2F1D05;
            margin-top: 0;
            margin-bottom: 20px;
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.78);
            backdrop-filter: blur(12px);
            padding: 24px;
            border-radius: 24px;
            box-shadow: 0 16px 35px rgba(181, 111, 32, 0.12);
            border: 1px solid rgba(255, 190, 104, 0.38);
            min-height: 155px;
        }

        .metric-top {
            display: flex;
            gap: 16px;
            align-items: center;
        }

        .metric-icon {
            width: 54px;
            height: 54px;
            border-radius: 18px;
            background: linear-gradient(135deg, #FFF1B8, #FFC46B);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 27px;
        }

        .metric-title {
            margin: 0;
            color: #80591C;
            font-size: 14px;
            font-weight: 700;
        }

        .metric-value {
            margin: 4px 0 0 0;
            color: #3B2506;
            font-size: 25px;
            font-weight: 850;
        }

        .metric-note {
            margin-top: 18px;
            margin-bottom: 0;
            color: #8B6A2D;
            font-size: 13px;
            line-height: 1.5;
        }

        .content-card,
        .empty-card {
            background: rgba(255, 255, 255, 0.80);
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

        label,
        .stRadio label,
        .stSelectbox label,
        .stDateInput label,
        .stNumberInput label,
        .stTextArea label {
            color: #4B3109 !important;
            font-weight: 700 !important;
            font-size: 15px !important;
        }

        div[data-testid="stRadio"] {
            background: rgba(255, 255, 255, 0.56);
            border: 1px solid rgba(255, 184, 77, 0.34);
            border-radius: 22px;
            padding: 18px 20px 10px 20px;
            margin-bottom: 16px;
            box-shadow: 0 12px 28px rgba(181, 111, 32, 0.08);
        }

        div[data-baseweb="select"] > div,
        div[data-testid="stTextInput"] input,
        div[data-testid="stNumberInput"] input,
        div[data-testid="stDateInput"] input,
        textarea {
            background-color: #FFFDF8 !important;
            color: #2F1D05 !important;
            border-radius: 16px !important;
            border: 1.5px solid rgba(255, 173, 72, 0.45) !important;
            box-shadow: 0 8px 20px rgba(180, 105, 20, 0.06) !important;
        }

        div[data-baseweb="select"] > div:hover,
        div[data-testid="stTextInput"] input:hover,
        div[data-testid="stNumberInput"] input:hover,
        div[data-testid="stDateInput"] input:hover,
        textarea:hover {
            border-color: rgba(255, 159, 28, 0.8) !important;
        }

        div[data-baseweb="select"] span {
            color: #2F1D05 !important;
        }

        input::placeholder,
        textarea::placeholder {
            color: #A98243 !important;
        }

        .stButton > button,
        .stFormSubmitButton > button {
            background: linear-gradient(135deg, #FFB13B, #FF9F1C);
            color: #2F1D05;
            border: none;
            border-radius: 18px;
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
            min-width: 210px;
            height: 54px;
        }

        .button-space {
            height: 8px;
        }

        .footer-note {
            text-align: center;
            color: #8B6A2D;
            font-size: 13px;
            margin-top: 42px;
        }

        div[data-testid="stDataFrame"] {
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 14px 30px rgba(181, 111, 32, 0.08);
        }

        @media screen and (max-width: 768px) {
            .hero-title {
                font-size: 32px;
            }

            .page-heading h1 {
                font-size: 28px;
            }

            div[data-testid="stForm"] {
                padding: 24px;
            }
        }
    </style>
    """, unsafe_allow_html=True)