from order import Order

class Customer:
    _all_customers = []  # Class variable to keep track of all customers

    def __init__(self, name):
        self._name = None
        self._orders = []  # List of orders placed by the customer
        self.name = name  # This will trigger the name setter
        Customer._all_customers.append(self)  # Track this customer

    # Property for 'name' with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    # Method to place an order
    def place_order(self, coffee, quantity):
        order = Order(self, coffee, quantity)  # Create a new order
        self._orders.append(order)
        coffee.add_order(order)  # Also add this order to the coffee
        return order

    # Method to return all orders placed by this customer
    def orders(self):
        return self._orders

    # Method to return all unique coffees ordered by this customer
    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    # Method to create a new order with a given coffee and quantity
    def create_order(self, coffee, quantity):
        order = Order(self, coffee, quantity)  # Create a new order with quantity
        self._orders.append(order)
        coffee.add_order(order)
        return order

    # Class method to find the customer who spent the most on a specific coffee
    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        top_customer = None

        for customer in cls._all_customers:
            total_spent = sum(order.coffee.price * order.quantity for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer

        return top_customer

    def __repr__(self):
        return f"Customer(name={self._name})"
