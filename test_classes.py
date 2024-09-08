from customer import Customer
from coffee import Coffee
from order import Order

# Test creating an order via Customer
def test_customer_create_order():
    customer1 = Customer("Alice")
    coffee1 = Coffee("Latte", 4.50)

    # Alice creates an order for Latte with a quantity of 2
    order1 = customer1.create_order(coffee1, 2)

    # Check that the order is created and associated correctly
    assert order1.quantity == 2
    assert order1.coffee == coffee1
    assert order1.customer == customer1
    assert len(customer1.orders()) == 1
    assert coffee1.num_orders() == 1

# Test num_orders and average_price for Coffee
def test_coffee_aggregate_methods():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee1 = Coffee("Cappuccino", 5.00)

    # Both Alice and Bob order Cappuccino
    customer1.create_order(coffee1, 1)
    customer2.create_order(coffee1, 2)

    # Check the total number of orders
    assert coffee1.num_orders() == 2

    # Check the average price (since price is always the same, average price will be the coffee price)
    assert coffee1.average_price() == 5.00

# Test the most_aficionado method
def test_most_aficionado():
    coffee1 = Coffee("Espresso", 3.00)
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Alice orders 1 Espresso, Bob orders 3 Espressos
    customer1.create_order(coffee1, 1)
    customer2.create_order(coffee1, 3)

    # Bob should be the aficionado since he spent the most
    assert Customer.most_aficionado(coffee1) == customer2
