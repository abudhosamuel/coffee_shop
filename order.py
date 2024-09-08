from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, quantity):
        self._customer = None
        self._coffee = None
        self._quantity = None
        self._price = None
        
        self.customer = customer  # Trigger customer setter
        self.coffee = coffee      # Trigger coffee setter
        self.quantity = quantity  # Set the quantity

    # Property for 'customer' with validation
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer  # Lazy import to avoid circular dependency
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of the Customer class.")
        self._customer = value

    # Property for 'coffee' with validation
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of the Coffee class.")
        self._coffee = value

    # Property for 'quantity' with validation
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self._quantity = value

    # Method to return order details including total price
    def get_order_details(self):
        return {
            'customer': self.customer.name,
            'coffee': self.coffee.name,
            'quantity': self.quantity,
            'total_price': self.coffee.price * self.quantity
        }

    def __repr__(self):
        return f"Order(customer={self._customer}, coffee={self._coffee}, quantity={self._quantity})"
