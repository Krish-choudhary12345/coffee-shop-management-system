class Coffee:
    # Initialize coffee with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    # Initialize order with an empty list
    def __init__(self):
        self.items = []

    # Add coffee to the order
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"{coffee.name} added to your order.")

    # Calculate total price
    def total_price(self):
        return sum(item.price for item in self.items)

    # Show order summary
    def show_order(self):
        if not self.items:
            print("\nNo items in your order.")
            return

        print("\n------ Your Order ------")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")

        print(f"\nTotal Price: ${self.total_price():.2f}")

    # Checkout process
    def checkout(self):
        if not self.items:
            print("\nYour cart is empty.")
            return

        self.show_order()

        confirm = input("\nProceed to checkout? (yes/no): ").strip().lower()

        if confirm == "yes":
            print("\nOrder confirmed!")
            print("Thank you for your purchase. ☕")
            self.items.clear()
        else:
            print("\nCheckout cancelled.")


def main():
    # Coffee Menu
    menu = [
        Coffee("Espresso", 2.50),
        Coffee("Latte", 3.50),
        Coffee("Cappuccino", 3.00),
        Coffee("Americano", 2.00)
    ]

    order = Order()

    while True:
        print("\n========== Coffee Menu ==========")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")

        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice in ["1", "2", "3", "4"]:
            order.add_item(menu[int(choice) - 1])

        elif choice == "5":
            order.show_order()

        elif choice == "6":
            order.checkout()

        elif choice == "7":
            print("\nThank you for visiting our Coffee Shop!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()