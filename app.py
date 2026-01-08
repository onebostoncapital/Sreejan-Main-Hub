import streamlit as st
import ccxt

st.set_page_config(page_title="Sreejan Hub", layout="centered")

# Rule 14: Theme Toggle
theme = st.sidebar.radio("Theme Mode", ["Dark Mode", "Light Mode"])
bg = "#000000" if theme == "Dark Mode" else "#FFFFFF"
txt = "#FFFFFF" if theme == "Dark Mode" else "#000000"
st.markdown(f"<style>.stApp {{ background-color: {bg}; color: {txt} !important; }} h1 {{ color: #D4AF37 !important; text-align: center; }}</style>", unsafe_allow_html=True)

# Fetch Prices for Banner
try:
    ex = ccxt.kraken()
    b_p = ex.fetch_ticker('BTC/USD')['last']
    s_p = ex.fetch_ticker('SOL/USD')['last']
except: b_p, s_p = 0, 0

# Rule 13: Universal Banner
st.title("🏛️ Sreejan Command Center")
h1, h2 = st.columns(2)
h1.metric("₿ BTC", f"${b_p:,.2f}")
h2.metric("S SOL", f"${s_p:,.2f}")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader("📉 Perp Terminal")
    st.link_button("LAUNCH", "https://defi-tuna-apper-bohsifbb9dawewnwd56uo5.streamlit.app/", use_container_width=True)
with col2:
    st.subheader("🔮 Range Model")
    st.link_button("LAUNCH", "https://sreejan-predictive-range-m3edgoybaeocgzsm6wykj7.streamlit.app/", use_container_width=True)
