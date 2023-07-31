import streamlit as st

# Define a function to clear the input
def clearInput(input_id):
    """Clears the input with the given ID."""
    st.session_state[input_id] = ''

# Set default text for the inputs
default_account_size = 0.0
default_max_stocks_portfolio = 6
default_trade_entry = 0.0
default_stoploss = 0.0
default_risk_percentage = 0.0

# Get user inputs
account_size = st.number_input("Enter your account size:", step=0.01, key="account_size", value=default_account_size, on_change=clearInput)
max_stocks_portfolio = st.number_input("Enter the maximum number of stocks in your portfolio:", step=1, key="max_stocks_portfolio", value=default_max_stocks_portfolio, on_change=clearInput)

# Get user inputs for a specific trade
trade_entry = st.number_input("Enter the trade entry point:", step=0.01, key="trade_entry", value=default_trade_entry, on_change=clearInput)
stoploss = st.number_input("Enter the stop loss price:", step=0.01, key="stoploss", value=default_stoploss, on_change=clearInput)
risk_percentage = st.number_input("Enter the percentage of capital you want to risk per trade:", step=0.01, key="risk_percentage", value=default_risk_percentage, on_change=clearInput)

# Rest of your code remains unchanged.
# ...

def main():
    # Your code goes here

if __name__ == "__main__":
    main()
