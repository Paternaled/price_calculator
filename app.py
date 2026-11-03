import streamlit as st

from calculator import combo_upgrade_cost, refund_by_items, refund_by_totals

st.title("Price Calculator")

st.sidebar.header("Tax settings")
tax_on = st.sidebar.checkbox("Include tax")
tax_percent = st.sidebar.number_input(
    "Tax rate (%)", min_value=0.0, value=8.25, step=0.25
)
tax_rate = 1 + tax_percent / 100

tab_totals, tab_items, tab_combo = st.tabs(["By totals", "By items", "Combo upgrade"])

with tab_totals:
    original = st.number_input(
        "Original total ($)", min_value=0.0, step=0.01, key="totals_original"
    )
    desired = st.number_input(
        "Correct total ($)", min_value=0.0, step=0.01, key="totals_desired"
    )
    refund = refund_by_totals(original, desired, tax_on, tax_rate)
    st.metric("Refund", f"${refund:.2f}")


with tab_items:
    prices_text = st.text_input(
        "Correct item prices, separated by commas", key="item_prices"
    )
    pieces = prices_text.split(",")
    item_prices = []
    if prices_text.strip():
        for piece in pieces:
            item_prices.append(float(piece))
    original = st.number_input("Original total ($)", key="items_total")
    refund = refund_by_items(item_prices, original, tax_on, tax_rate)
    st.metric("Refund", f"{refund:.2f}")

with tab_combo:
    combo_price = st.number_input(
        "Combo price ($)", min_value=0.0, step=0.01, key="combo_price"
    )
    sandwich_price = st.number_input(
        "Sandwich price ($)", min_value=0.0, step=0.01, key="sandwich_price"
    )
    side_price = st.number_input(
        "Drink or fry price ($)", min_value=0.0, step=0.01, key="side_price"
    )
    upgrade_cost = combo_upgrade_cost(combo_price, sandwich_price, side_price)
    st.metric("Upgrade cost", f"${upgrade_cost:.2f}")
