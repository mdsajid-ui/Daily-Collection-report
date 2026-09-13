import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="DV Analytics | Daily Collection Intelligence",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Authentication credentials
DEFAULT_USER = "sk"
DEFAULT_PASS = "md"

valid_username = st.secrets.get("APP_USERNAME", os.environ.get("APP_USERNAME", DEFAULT_USER))
valid_password = st.secrets.get("APP_PASSWORD", os.environ.get("APP_PASSWORD", DEFAULT_PASS))

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

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

if not st.session_state.authenticated:
    _, col_form, _ = st.columns([1, 1.2, 1])
    with col_form:
        st.markdown("<h2 style='text-align:center; color:#2fd9e8; margin-top:15vh;'>DV Analytics Login</h2>", unsafe_allow_html=True)
        with st.form("login_form"):
            username = st.text_input("USERNAME", placeholder="Enter username")
            password = st.text_input("PASSWORD", type="password", placeholder="Enter password")
            submit = st.form_submit_button("Access Dashboard", use_container_width=True)
            if submit:
                if username == valid_username and password == valid_password:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
else:
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            dashboard_html = f.read()
        components.html(dashboard_html, height=1800, scrolling=True)
    else:
        st.error(f"Dashboard file not found at {html_path}")
