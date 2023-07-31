import streamlit as st

# Define a function to clear the input
def clearInput(input_id):
    """Clears the input with the given ID."""
    st.session_state[input_id] = ''

def main():
    # Set default text for the inputs
    default_account_size = 100000.0
    default_max_stocks_portfolio = 10
    default_trade_entry = 100.0
    default_stoploss = 95.0
    default_risk_percentage = 2.0

    # Get user inputs
    account_size = st.number_input("Enter your account size:", step=0.01, key="account_size", value=default_account_size, on_change=lambda: clearInput("account_size"))
    max_stocks_portfolio = st.number_input("Enter the maximum number of stocks in your portfolio:", step=1, key="max_stocks_portfolio", value=default_max_stocks_portfolio, on_change=lambda: clearInput("max_stocks_portfolio"))

    # Get user inputs for a specific trade
    trade_entry = st.number_input("Enter the trade entry point:", step=0.01, key="trade_entry", value=default_trade_entry, on_change=lambda: clearInput("trade_entry"))
    stoploss = st.number_input("Enter the stop loss price:", step=0.01, key="stoploss", value=default_stoploss, on_change=lambda: clearInput("stoploss"))
    risk_percentage = st.number_input("Enter the percentage of capital you want to risk per trade:", step=0.01, key="risk_percentage", value=default_risk_percentage, on_change=lambda: clearInput("risk_percentage"))

    # Rest of your code remains unchanged.
    # ...

if __name__ == "__main__":
    main()
