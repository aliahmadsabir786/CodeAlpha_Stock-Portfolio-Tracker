stock_price = {
    "APPLE": 140,
    "AMAZON": 207,
    "GOOGLE": 340,
    "MICROSOFT": 408,
    "TESLA": 650,
    "TOYATA": 540
}

Portfolio = []

def add_stock():
    stock_name = input("Enter stock symbol (e.g., APPLE, TESLA): ").upper()
    if stock_name not in stock_price:
        print("❌ There is no stock available.\n")
        return

    try:
        quantity = int(input("Enter Quantity: "))  # Fix: convert to int
        price = stock_price[stock_name]
        total = quantity * price  # Fix: ensure quantity is numeric
        Portfolio.append({
            "symbol": stock_name,
            "quantity": quantity,
            "price": price,
            "total": total,
        })
        print(f"✅ {stock_name} added successfully.\n")
    except ValueError:
        print("❌ Please enter a valid numeric quantity.\n")

def display_portfolio():
    if not Portfolio:
        print("📭 Portfolio is empty.\n")
        return

    print("📈 Your Stock Portfolio:\n")
    print(f"{'Symbol':<10}{'Quantity':<10}{'Price--$':<10}{'Total'}")
    grand_total = 0

    for stock in Portfolio:
        print(f"{stock['symbol']:<10}{stock['quantity']:<10}{stock['price']:<10}{stock['total']}")
        grand_total += stock['total']

    print(f"\n💰 Total Investment Value: ${grand_total:.2f}\n")

def save_file(filename="Portfolio.txt"):
    if not Portfolio:
        print("📭 No data to save in the file.\n")
        return  # Fix: Must return here if portfolio is empty

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Summary:\n")
            file.write(f"{'Symbol':<10}{'Quantity':<10}{'Price--$':<10}{'Total'}\n")
            total = 0
            for stock in Portfolio:
                line = f"{stock['symbol']:<10}{stock['quantity']:<10}{stock['price']:<10}{stock['total']}\n"
                file.write(line)
                total += stock['total']
            file.write(f"\nTotal Investment: ${total:.2f}\n")
        print(f"✅ Portfolio saved to {filename}\n")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def main():
    while True:
        print("=== 📊 Stock Portfolio Tracker ===")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Save to File")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_stock()
        elif choice == '2':
            display_portfolio()
        elif choice == '3':
            save_file()
        elif choice == '4':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# 🚀 Start the program
if __name__ == "__main__":
    main()
