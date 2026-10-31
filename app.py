import streamlit as st

st.title("Price Calculator")

st.sidebar.header("Tax settings")
tax_on = st.sidebar.checkbox("Include tax")
tax_percent = st.sidebar.number_input(
    "Tax rate(%)", min_value=0.0, value=8.25, step=0.25
)
tax_rate = 1 + tax_percent / 100

st.write(f"Tax on {tax_on}, rate multiplier: {tax_rate}")