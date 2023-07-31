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

    # Calculate position size and round it to the nearest 1st digit
    stop_difference = trade_entry - stoploss

    if stop_difference == 0:
        st.warning("Stop loss cannot be equal to trade entry. Please provide different inputs.")
        return

    position_size = round((account_size * (risk_percentage / 100)) / stop_difference, 1)

    # Calculate total buy value
    total_buy_value = round(position_size * trade_entry)

    # Calculate the percentage of the capital used for this trade
    percentage_used = round((total_buy_value / account_size) * 100, 2)

    # Calculate how much money will be at risk per trade
    money_at_risk_per_trade = round(position_size * stop_difference, 2)

    # Display the results
    st.write("Account size:", account_size)
    st.write("Maximum number of stocks in portfolio:", max_stocks_portfolio)
    st.write("Trade entry point:", trade_entry)
    st.write("Stop loss price:", stoploss)
    st.write("Risk percentage per trade:", risk_percentage)
    st.write("Position size per stock:", position_size, "Shares")
    st.write("Total buy value:", total_buy_value)
    st.write("Percentage of capital used for this trade:", percentage_used, "%")
    st.write("Money at risk per trade:", money_at_risk_per_trade)

if __name__ == "__main__":
    main()
