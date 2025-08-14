import random
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self, change):
        self.price += change

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class StockMarket:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock_name, price):
        self.stocks[stock_name] = Stock(stock_name, price)

    def process_order(self, stock_name, order_type, quantity):
        if stock_name in self.stocks:
            stock = self.stocks[stock_name]
            price_change = self.calculate_price_change(order_type, quantity)
            stock.update_price(price_change)
            print(f"Processed {order_type} order of {quantity} for {stock_name}. New price: ${stock.price:.2f}")
        else:
            print(f"Stock {stock_name} does not exist in the market.")

    def calculate_price_change(self, order_type, quantity):
        change = 10 * quantity  if order_type == "buy" else -10 * quantity
        return change

    def show_market(self):
        for stock in self.stocks.values():
            print(stock)


if __name__ == "__main__":
    market = StockMarket()

    # stocks
    market.add_stock("Gold", 5160.00)
    market.add_stock("Oil", 2200.00)
    market.add_stock("Silver", 1200.00)
    market.add_stock("Coffee", 900.00)

    # Prices_init
    print("Initial Market:")
    market.show_market()

    while True:
        stock_name = input("\nEnter the stock name you want to trade (or 'exit' to quit): ")
        if stock_name.lower() == 'exit':
            break

        if stock_name not in market.stocks:
            print(f"Stock {stock_name} does not exist in the market. Try again.")
            continue

        order_type = input("Enter order type ('buy' or 'sell'): ").lower()
        quantity = int(input("Enter the quantity: "))

        market.process_order(stock_name, order_type, quantity)

        # Updated Market
        print("\nUpdated Market:")
        market.show_market()
