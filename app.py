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

    /* === LUXURY BOTANICAL LOGIN PAGE STYLING === */
    .login-wrapper {
        min-height: 100vh;
        width: 100vw;
        display: flex;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle at 50% 50%, #1e2e28 0%, #0c1613 60%, #060a08 100%);
        padding: 20px;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    .login-card {
        width: 860px;
        max-width: 95vw;
        min-height: 520px;
        background: #FFFFFF;
        border-radius: 28px;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45), 0 0 1px rgba(255,255,255,0.2);
        display: flex;
        overflow: hidden;
        position: relative;
    }

    .login-left {
        flex: 1.15;
        padding: 44px 48px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background: #FFFFFF;
        color: #1a202c;
        z-index: 2;
    }

    .login-title {
        font-size: 28px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 24px;
        letter-spacing: -0.5px;
    }

    .login-subtitle {
        font-size: 13px;
        color: #64748b;
        margin-top: -18px;
        margin-bottom: 22px;
    }

    .login-right {
        flex: 0.95;
        background: linear-gradient(145deg, #1b332b, #0f211b);
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .login-divider {
        display: flex;
        align-items: center;
        text-align: center;
        margin: 20px 0 16px;
        color: #94a3b8;
        font-size: 12px;
    }
    .login-divider::before, .login-divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid #e2e8f0;
    }
    .login-divider span {
        padding: 0 12px;
        font-size: 11px;
        text-transform: lowercase;
    }

    .sso-row {
        display: flex;
        justify-content: center;
        gap: 14px;
        margin-bottom: 16px;
    }
    .sso-badge {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #f8fafc;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }

    .forgot-link {
        text-align: center;
        font-size: 11.5px;
        color: #0d9488;
        text-decoration: none;
        font-weight: 500;
    }

    /* Streamlit Form Restyling to match Left Card */
    div[data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
        background: transparent !important;
    }
    div[data-testid="stTextInput"] input {
        background-color: #f8fafc !important;
        border: 1.5px solid #e2e8f0 !important;
        border-radius: 12px !important;
        color: #0f172a !important;
        font-size: 13.5px !important;
        padding: 10px 14px !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #1f3d33 !important;
        box-shadow: 0 0 0 3px rgba(31, 61, 51, 0.15) !important;
    }
    div[data-testid="stTextInput"] label {
        color: #475569 !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        margin-bottom: 2px !important;
    }
    div[data-testid="stFormSubmitButton"] button {
        background: #233d32 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 10px 24px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        width: 100% !important;
        box-shadow: 0 4px 14px rgba(35, 61, 50, 0.35) !important;
        transition: all 0.2s ease !important;
        margin-top: 8px !important;
    }
    div[data-testid="stFormSubmitButton"] button:hover {
        background: #1b3027 !important;
        box-shadow: 0 6px 18px rgba(35, 61, 50, 0.5) !important;
        transform: translateY(-1px) !important;
    }

    @media (max-width: 768px) {
        .login-card {
            flex-direction: column;
            width: 100%;
            border-radius: 20px;
        }
        .login-right {
            display: none;
        }
        .login-left {
            padding: 32px 24px;
        }
    }
</style>
""", unsafe_allow_html=True)

if not st.session_state.authenticated:
    st.markdown("""
    <div class="login-wrapper">
      <div class="login-card">
        <div class="login-left">
          <div class="login-title">Log in</div>
          <div class="login-subtitle">DV Analytics • Daily Collection Intelligence</div>
    """, unsafe_allow_html=True)

    with st.form("custom_login_form"):
        username = st.text_input("Login, email or username", value="", placeholder="Enter username (e.g. sk)")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        submit = st.form_submit_button("Log in", use_container_width=True)
        if submit:
            if username == valid_username and password == valid_password:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid username or password. (Default: sk / md)")

    st.markdown("""
          <div class="login-divider">
            <span>or log in with</span>
          </div>

          <div class="sso-row">
            <div class="sso-badge" title="Google SSO">
              <svg width="18" height="18" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
              </svg>
            </div>
            <div class="sso-badge" title="Microsoft 365">
              <svg width="18" height="18" viewBox="0 0 24 24">
                <path fill="#F25022" d="M1 1h10v10H1z"/>
                <path fill="#7FBA00" d="M13 1h10v10H13z"/>
                <path fill="#00A4EF" d="M1 13h10v10H1z"/>
                <path fill="#FFB900" d="M13 13h10v10H13z"/>
              </svg>
            </div>
          </div>

          <div class="forgot-link">
            Forgot login or password?
          </div>
        </div>

        <!-- Right Botanical Art Panel -->
        <div class="login-right">
          <svg viewBox="0 0 400 600" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="position:absolute; top:0; left:0; width:100%; height:100%;">
            <defs>
              <linearGradient id="leafGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#2d5244" />
                <stop offset="100%" stop-color="#142820" />
              </linearGradient>
              <linearGradient id="leafGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3d6c5a" />
                <stop offset="100%" stop-color="#1c382e" />
              </linearGradient>
              <linearGradient id="leafGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#4e8872" />
                <stop offset="100%" stop-color="#274d3f" />
              </linearGradient>
              <filter id="dropShadow" x="-20%" y="-20%" width="140%" height="140%">
                <feDropShadow dx="-4" dy="6" stdDeviation="8" flood-color="#050a08" flood-opacity="0.6"/>
              </filter>
            </defs>

            <!-- Layer 1: Background Deep Green -->
            <rect width="400" height="600" fill="#142820" />

            <!-- Layer 2: Deep foliage silhouettes -->
            <g filter="url(#dropShadow)" opacity="0.85">
              <path d="M400,100 C300,150 220,280 260,420 C290,520 380,580 400,600 L400,100 Z" fill="url(#leafGrad1)"/>
              <path d="M400,0 C280,40 180,180 210,320 C230,420 340,540 400,560 Z" fill="url(#leafGrad2)"/>
            </g>

            <!-- Layer 3: Organic Cutout Waves (matching Image 2) -->
            <g filter="url(#dropShadow)">
              <!-- White paper edge curve -->
              <path d="M0,0 L80,0 C140,120 40,240 110,360 C160,450 90,540 70,600 L0,600 Z" fill="#ffffff" opacity="0.04"/>
              <path d="M400,200 C260,220 160,340 190,460 C210,540 320,600 400,600 Z" fill="url(#leafGrad3)"/>
            </g>

            <!-- Layer 4: Tropical Palm/Fern Fronds -->
            <g stroke="#2d5244" stroke-width="2" fill="none" opacity="0.65">
              <!-- Stem 1 -->
              <path d="M380,120 Q280,240 220,380" stroke-width="3" stroke="#4e8872"/>
              <path d="M280,240 L250,210 M280,240 L310,210 M260,270 L220,250 M260,270 L290,240 M240,310 L200,300 M240,310 L270,280 M225,350 L180,350 M225,350 L250,330"/>
              <!-- Stem 2 -->
              <path d="M400,350 Q260,420 180,520" stroke-width="3" stroke="#4e8872"/>
              <path d="M320,390 L290,360 M320,390 L340,350 M280,420 L240,400 M280,420 L300,380 M240,460 L190,450 M240,460 L250,420 M200,500 L150,500 M200,500 L210,470"/>
            </g>
          </svg>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
else:
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            dashboard_html = f.read()
        components.html(dashboard_html, height=1800, scrolling=True)
    else:
        st.error(f"Dashboard file not found at {html_path}")
