import streamlit as st

def main():
    st.title("Position Sizing Calculator")

    # Get user inputs
    account_size = st.number_input("Enter your account size:", step=0.01)
    max_stocks_portfolio = st.number_input("Enter the maximum number of stocks in your portfolio:", step=1)

    # Get user inputs for a specific trade
    trade_entry = st.number_input("Enter the trade entry point:", step=0.01)
    stoploss = st.number_input("Enter the stop loss price:", step=0.01)
    risk_percentage = st.number_input("Enter the percentage of capital you want to risk per trade:", step=0.01)

    # Store the value of the click
    clear_inputs = st.button("Clear Inputs")

    # Check if the button was clicked, then set the input values to blank
    if clear_inputs:
        account_size = ""
        max_stocks_portfolio = ""
        trade_entry = ""
        stoploss = ""
        risk_percentage = ""

    # Convert the input fields back to numeric values if they are not empty strings
    account_size_str = str(account_size)
    if account_size_str == "":
        account_size = 0.0
    else:
        account_size = float(account_size_str)

    # Check if the input fields are empty
    if account_size != 0.0:
    
        stop_difference = trade_entry - stoploss

        if stop_difference == 0:
            st.warning("Stop loss cannot be equal to trade entry. Please provide different inputs.")
            return

        position_size = round((account_size * (risk_percentage / 100)) / stop_difference, 1)
    else:
        position_size = ""

    # Display the results
    st.write("Account size:", account_size)
    st.write("Maximum number of stocks in portfolio:", max_stocks_portfolio)
    st.write("Trade entry point:", trade_entry)
    st.write("Stop loss price:", stoploss)
    st.write("Risk percentage per trade:", risk_percentage)
    st.write("Position size per stock:", position_size, "Shares")

if __name__ == "__main__":
    main()
