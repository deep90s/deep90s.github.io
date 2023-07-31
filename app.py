# Get user inputs
account_size = float(input("Enter your account size: "))
max_stocks_portfolio = int(
  input(
    "Enter the maximum number of stocks you want to keep in your portfolio: "))

# Calculate capital per stock
capital_per_stock = round(account_size / max_stocks_portfolio)
print("Capital per stock:", capital_per_stock)
# Get user inputs for a specific trade
trade_entry = float(input("Enter the trade entry point: "))
stoploss = float(input("Enter the stop loss price: "))
risk_percentage = float(
  input("Enter the percentage of capital you want to risk per trade: "))

# Calculate position size and round it to the nearest 1st digit
stop_difference = trade_entry - stoploss
position_size = round(
  (account_size * (risk_percentage / 100)) / stop_difference, 1)

# Calculate total buy value
total_buy_value = round(position_size * trade_entry)

# Calculate the percentage of the capital used for this trade
percentage_used = round((total_buy_value / account_size) * 100, 2)

# Print the results
print("\nAccount size:", account_size)
print("Maximum number of stocks in portfolio:", max_stocks_portfolio)

print("Trade entry point:", trade_entry)
print("Stop loss price:", stoploss)
print("Risk percentage per trade:", risk_percentage)
print("Position size per stock:", position_size, "Shares")
print("Total buy value:", total_buy_value)
print("Percentage of capital used for this trade:", percentage_used, "%")
