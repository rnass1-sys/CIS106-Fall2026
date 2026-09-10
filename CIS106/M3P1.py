# Program to calculate total stock investment amount

# Input section
ticker = input("Enter the stock ticker symbol (e.g., MSFT): ")
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

# Processing section
amount_invested = shares * cost_per_share

# Output section
print(f"\nStock Ticker: {ticker}")
print(f"Amount Invested: ${amount_invested:.2f}")
