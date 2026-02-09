import streamlit as st
from tools import get_currency, get_exchange_rates, get_index_value
from llm import get_market_data

st.set_page_config(page_title="Country Finance Agent", layout="wide")

st.title("🌍 Currency & Stock Market Agent")

country = st.text_input("Enter any country")

if st.button("Analyze") and country:
    with st.spinner("Fetching data..."):
        currency_code, currency_name = get_currency(country)
        fx = get_exchange_rates(currency_code)
        market = get_market_data(country)

    st.subheader("💰 Official Currency")
    st.write(f"{currency_name} ({currency_code})")

    st.subheader("💱 Exchange Rates (1 unit)")
    st.json(fx)

    st.subheader("🏦 Major Stock Exchanges")
    for ex in market["exchanges"]:
        st.write("•", ex)

    st.subheader("📈 Stock Indices")
    for name, symbol in market["indices"].items():
        value = get_index_value(symbol)
        st.write(f"**{name}** ({symbol}): {value}")

    st.subheader("🗺 Exchange HQ Locations")
    for ex in market["exchanges"]:
        map_url = f"https://www.google.com/maps?q={ex}&output=embed"
        st.components.v1.iframe(map_url, height=300)
