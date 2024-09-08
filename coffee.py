class Coffee:
    def __init__(self, name, price):
        self._name = None
        self._orders = []  # List of orders for this coffee
        self.name = name  # This will trigger the name setter
        self.price = price  # Price of the coffee

    # Property for 'name' with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value

    def add_order(self, order):
        self._orders.append(order)

    # Method to return all orders for this coffee
    def orders(self):
        return self._orders

    # Method to return all unique customers for this coffee
    def customers(self):
        return list(set(order.customer for order in self._orders))

    # Method to return the total number of orders for this coffee
    def num_orders(self):
        return len(self._orders)

    # Method to return the average price for this coffee based on orders
    def average_price(self):
        if not self._orders:
            return 0
        # Calculate the total price by multiplying coffee price with order quantity
        total_price = sum(order.coffee.price * order.quantity for order in self._orders)
        total_quantity = sum(order.quantity for order in self._orders)
        return total_price / total_quantity

    def __repr__(self):
        return f"Coffee(name={self._name}, price={self.price})"
