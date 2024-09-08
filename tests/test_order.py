from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Latte", 4.50)
    order = Order(customer, coffee, 2)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.quantity == 2

def test_order_price_validation():
    try:
        customer = Customer("Alice")
        coffee = Coffee("Latte", 4.50)
        order = Order(customer, coffee, -1)
    except ValueError as e:
        assert str(e) == "Quantity must be a positive integer."

def test_order_get_order_details():
    customer = Customer("Alice")
    coffee = Coffee("Latte", 4.50)
    order = Order(customer, coffee, 2)

    details = order.get_order_details()
    assert details['customer'] == "Alice"
    assert details['coffee'] == "Latte"
    assert details['quantity'] == 2
    assert details['total_price'] == 9.00  # 4.50 * 2
