import streamlit as st

st.set_page_config(page_title="Sreejan Command Center", layout="centered")

# Master UI Styling (True Black & Gold)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF !important; }
    h1 { color: #D4AF37 !important; text-align: center; font-family: 'Libre Baskerville'; }
    p { text-align: center; font-size: 18px; color: #888; }
    .hub-container { padding: 50px; border: 1px solid #333; border-radius: 20px; background: #050505; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="hub-container">', unsafe_allow_html=True)
st.title("🏛️ Sreejan Command Center")
st.write("Select a terminal to begin your session.")

st.divider()

# Create two big columns for the buttons
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📉 Perp Trading")
    st.write("Emmanuel-Logic Signals & Technical Charting")
    # REPLACE THE URL BELOW WITH YOUR ACTUAL PERP INDICATOR LINK
    st.link_button("Open Perp Terminal", "https://your-perp-app-link.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("### 🔮 Range Model")
    st.write("Predictive Yield & Liquidation Safety")
    # REPLACE THE URL BELOW WITH YOUR ACTUAL RANGE MODEL LINK
    st.link_button("Open Range Model", "https://your-range-app-link.streamlit.app/", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.caption("Secure Institutional Environment | v1.0 | 2026")
