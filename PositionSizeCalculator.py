import streamlit as st
# The AdSense code snippet you copied
adsense_code = """ <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1846635093121225"
     crossorigin="anonymous"></script> """

# Embed the AdSense code using markdown with unsafe_allow_html
st.markdown(adsense_code, unsafe_allow_html=True)
def main():
    st.title("Position Sizing Calculator")

    # Clear the input box when clicked using JavaScript
    st.markdown(
        """
        <script>
        function clearInput(id) {
            document.getElementById(id).value = "";
        }
        </script>
        """,
        unsafe_allow_html=True
    )

    # Get user inputs
    account_size = st.number_input("Enter your account size:", step=0.01, key="account_size", on_change=clearInput)
    max_stocks_portfolio = st.number_input("Enter the maximum number of stocks in your portfolio:", step=1, key="max_stocks_portfolio", on_change=clearInput)

    # Get user inputs for a specific trade
    trade_entry = st.number_input("Enter the trade entry point:", step=0.01, key="trade_entry", on_change=clearInput)
    stoploss = st.number_input("Enter the stop loss price:", step=0.01, key="stoploss", on_change=clearInput)
    risk_percentage = st.number_input("Enter the percentage of capital you want to risk per trade:", step=0.01, key="risk_percentage", on_change=clearInput)

    # Rest of your code remains unchanged.
    # ...

if __name__ == "__main__":
    main()
