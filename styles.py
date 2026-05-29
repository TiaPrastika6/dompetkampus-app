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

        [data-testid="stToolbar"] {
            display: none;
        }

        [data-testid="stDecoration"] {
            display: none;
        }

        [data-testid="stStatusWidget"] {
            display: none;
        }

        .stDeployButton {
            display: none;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        .stApp {
            background: linear-gradient(135deg, #FFF8E7 0%, #FFF2D2 45%, #FFE7B0 100%);
            color: #3A2A12;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FFF1C9 0%, #FFE0A3 100%);
            border-right: 1px solid rgba(255, 166, 77, 0.25);
        }

        section[data-testid="stSidebar"] * {
            color: #4A3210;
        }

        .hero-card {
            background: linear-gradient(135deg, #FFB84D 0%, #FFD166 55%, #FFE8A3 100%);
            padding: 34px 38px;
            border-radius: 28px;
            box-shadow: 0 20px 45px rgba(214, 132, 27, 0.18);
            margin-bottom: 30px;
            border: 1px solid rgba(255, 255, 255, 0.55);
        }

        .hero-title {
            font-size: 42px;
            font-weight: 850;
            margin: 0;
            color: #3B2506;
            letter-spacing: -1px;
        }

        .hero-subtitle {
            font-size: 16px;
            margin-top: 10px;
            margin-bottom: 0;
            color: #5C4218;
            max-width: 780px;
            line-height: 1.7;
            font-weight: 500;
        }

        .section-title {
            font-size: 26px;
            font-weight: 800;
            color: #3A2A12;
            margin-bottom: 18px;
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
        .empty-card,
        div[data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.78);
            padding: 26px;
            border-radius: 26px;
            box-shadow: 0 16px 35px rgba(181, 111, 32, 0.12);
            border: 1px solid rgba(255, 190, 104, 0.35);
            margin-bottom: 20px;
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

        .stButton > button,
        .stFormSubmitButton > button {
            background: linear-gradient(135deg, #FFB84D, #FF9F1C);
            color: #3B2506;
            border: none;
            border-radius: 16px;
            padding: 0.75rem 1.2rem;
            font-weight: 800;
            box-shadow: 0 12px 24px rgba(255, 159, 28, 0.28);
            transition: all 0.2s ease;
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 16px 30px rgba(255, 159, 28, 0.35);
            color: #3B2506;
        }

        div[data-baseweb="select"] > div,
        div[data-testid="stTextInput"] input,
        div[data-testid="stNumberInput"] input,
        div[data-testid="stDateInput"] input,
        textarea {
            background-color: #FFFFFF !important;
            color: #3A2A12 !important;
            border-radius: 14px !important;
            border: 1px solid rgba(255, 165, 65, 0.45) !important;
        }

        div[data-baseweb="select"] span {
            color: #3A2A12 !important;
        }

        label,
        .stRadio label,
        .stSelectbox label,
        .stDateInput label,
        .stNumberInput label,
        .stTextArea label {
            color: #5A3B0B !important;
            font-weight: 600 !important;
        }

        input::placeholder,
        textarea::placeholder {
            color: #9A7A45 !important;
        }

        .footer-note {
            text-align: center;
            color: #8B6A2D;
            font-size: 13px;
            margin-top: 40px;
        }
    </style>
    """, unsafe_allow_html=True)