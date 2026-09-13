import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="DV Analytics | Daily Collection Intelligence",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-color: #090c16 !important;
        color: #FFFFFF !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    .main .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        width: 100vw !important;
    }
    iframe {
        width: 100% !important;
        height: 100vh !important;
        min-height: 100vh !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

html_path = os.path.join(os.path.dirname(__file__), "index.html")
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        dashboard_html = f.read()
    components.html(dashboard_html, height=1900, scrolling=True)
else:
    st.error(f"Dashboard file not found at {html_path}")
