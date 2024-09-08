from coffee import Coffee
from customer import Customer

def test_coffee_initialization():
    coffee = Coffee("Cappuccino", 5.00)
    assert coffee.name == "Cappuccino"
    assert coffee.price == 5.00

def test_coffee_name_validation():
    try:
        coffee = Coffee("T", 4.50)
    except ValueError as e:
        assert str(e) == "Name must be at least 3 characters long."

def test_coffee_num_orders():
    coffee = Coffee("Cappuccino", 5.00)
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Both customers order Cappuccino
    customer1.create_order(coffee, 1)
    customer2.create_order(coffee, 2)

    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Cappuccino", 5.00)
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Alice orders 1, Bob orders 2
    customer1.create_order(coffee, 1)
    customer2.create_order(coffee, 2)

    # The average price should be the price of the coffee since all have the same price
    assert coffee.average_price() == 5.00
