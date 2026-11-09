# Price Calculator

A Streamlit app that helps fast-food managers quickly work out refunds and combo upgrade charges, such as when a customer was charged the wrong total or missed an item. I built it to speed up refund math at the register, which I was doing by hand.

**Live app:** https://refund-calculator.streamlit.app/

## Features

- **Refund by totals**: enter what the customer was charged and what they should have paid.
- **Refund by items**: enter the correct item prices and the original total.
- **Combo upgrade cost**: enter the combo price, sandwich price, and side price to get the amount to charge for upgrading to the full combo.
- **Tax settings**: turn tax on or off and set the tax rate.

## How it's built

All calculations live in `calculator.py`, separate from the user interfaces. The Streamlit web app (`app.py`) and the terminal app (`cli.py`) both import from it, so the math is written once and shared. The calculations are covered by automated tests with pytest.

## Run it locally

```bash
git clone https://github.com/Paternaled/price_calculator.git
cd price_calculator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

To use the terminal version instead:

```bash
python cli.py
```

## Run the tests

```bash
python -m pytest
```