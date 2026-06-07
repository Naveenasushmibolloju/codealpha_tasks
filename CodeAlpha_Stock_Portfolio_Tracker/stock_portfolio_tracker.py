import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:

    stock_name = input("\nEnter Stock Symbol: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    investment = stock_prices[stock_name] * quantity

    if stock_name in portfolio:
        portfolio[stock_name]["Quantity"] += quantity
        portfolio[stock_name]["Investment"] += investment
    else:
        portfolio[stock_name] = {
            "Quantity": quantity,
            "Price": stock_prices[stock_name],
            "Investment": investment
        }

    total_investment += investment

    choice = input("\nDo you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n" + "=" * 50)
print("          PORTFOLIO SUMMARY")
print("=" * 50)

for stock, details in portfolio.items():
    print(
        f"{stock} | Qty: {details['Quantity']} | "
        f"Price: ${details['Price']} | "
        f"Value: ${details['Investment']}"
    )

print("\nTotal Investment Value: $", total_investment)

# Save portfolio to CSV file
with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Stock", "Quantity", "Price", "Investment Value"]
    )

    for stock, details in portfolio.items():

        writer.writerow([
            stock,
            details["Quantity"],
            details["Price"],
            details["Investment"]
        ])

    # Total row
    writer.writerow(["Total", "", "", total_investment])

print("\nPortfolio saved successfully to portfolio.csv")
