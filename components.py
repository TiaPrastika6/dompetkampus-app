import streamlit as st


def metric_card(title, value, icon, note):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-top">
                <div class="metric-icon">{icon}</div>
                <div>
                    <p class="metric-title">{title}</p>
                    <h2 class="metric-value">{value}</h2>
                </div>
            </div>
            <p class="metric-note">{note}</p>
        </div>
        """,
        unsafe_allow_html=True
    )