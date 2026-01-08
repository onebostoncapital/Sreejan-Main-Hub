import streamlit as st

# Configure the page
st.set_page_config(page_title="Sreejan Command Center", layout="centered")

# MASTER UI STYLING (True Black & Gold High Contrast)
st.markdown("""
    <style>
    /* Global Background */
    .stApp { background-color: #000000; color: #FFFFFF !important; }
    
    /* Center and Style the Title */
    h1 { color: #D4AF37 !important; text-align: center; font-family: 'Georgia', serif; font-size: 42px; margin-bottom: 10px; }
    
    /* Subtitle text */
    .subtitle { text-align: center; font-size: 18px; color: #888; margin-bottom: 40px; }
    
    /* The Box Container */
    .hub-container { 
        padding: 40px; 
        border: 2px solid #333; 
        border-radius: 20px; 
        background: #050505; 
        box-shadow: 0px 4px 20px rgba(212, 175, 55, 0.1);
    }

    /* Style for the Section Titles */
    h3 { color: #FFFFFF !important; margin-bottom: 5px; }
    .desc { color: #AAAAAA; font-size: 14px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Main Container Start
st.markdown('<div class="hub-container">', unsafe_allow_html=True)

st.markdown("<h1>🏛️ Sreejan Command Center</h1>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Secure Institutional Gateway for SOL/BTC Trading Systems</div>', unsafe_allow_html=True)

st.divider()

# Create two columns for the navigation buttons
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📉 Perp Indicator")
    st.markdown('<div class="desc">Emmanuel-Logic: 20 EMA / 200 SMA High-Frequency Signals</div>', unsafe_allow_html=True)
    # Your specific link integrated below
    st.link_button("LAUNCH PERP TERMINAL", "https://defi-tuna-apper-bohsifbb9dawewnwd56uo5.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("### 🔮 Range Model")
    st.markdown('<div class="desc">Predictive Yield Logic & 45% Liquidation Safety Floor</div>', unsafe_allow_html=True)
    # Your specific link integrated below
    st.link_button("LAUNCH RANGE MODEL", "https://sreejan-predictive-range-m3edgoybaeocgzsm6wykj7.streamlit.app/", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.caption("Terminal Status: ONLINE | Version 1.0.0 | High-Contrast Mode Enabled")
