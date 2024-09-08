from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte", 4.50)
    
    order = customer.place_order(coffee, 2)
    
    # Use the correct method
    assert len(customer.orders()) == 1
    assert customer.orders()[0].coffee == coffee
    assert order.get_order_details()['total_price'] == 9.00

def test_coffee_order():
    customer = Customer("Bob")
    coffee = Coffee("Espresso", 3.00)
    
    order = customer.place_order(coffee, 3)
    
    # Call the 'orders()' method instead of accessing 'orders' as an attribute
    assert len(coffee.orders()) == 1
    assert coffee.orders()[0].quantity == 3
    assert order.get_order_details()['total_price'] == 9.00
