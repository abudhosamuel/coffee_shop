from customer import Customer
from coffee import Coffee

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    try:
        customer = Customer("")
    except ValueError as e:
        assert str(e) == "Name must be between 1 and 15 characters."

def test_customer_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte", 4.50)
    order = customer.create_order(coffee, 2)
    
    assert len(customer.orders()) == 1
    assert order.coffee == coffee
    assert order.quantity == 2

def test_customer_most_aficionado():
    coffee = Coffee("Espresso", 3.00)
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Alice orders 1 Espresso, Bob orders 3 Espressos
    customer1.create_order(coffee, 1)
    customer2.create_order(coffee, 3)

    # Bob should be the aficionado since he spent the most
    assert Customer.most_aficionado(coffee) == customer2
