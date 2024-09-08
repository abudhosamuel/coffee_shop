from customer import Customer
from coffee import Coffee
from order import Order

# Debugging and testing code interactively
def main():
    # Create a Customer
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create some Coffee instances
    latte = Coffee("Latte", 4.50)
    cappuccino = Coffee("Cappuccino", 5.00)

    # Place some orders
    alice_order1 = alice.create_order(latte, 2)  # Alice orders 2 Lattes
    bob_order1 = bob.create_order(cappuccino, 3)  # Bob orders 3 Cappuccinos

    # Print order details
    print(alice_order1.get_order_details())
    print(bob_order1.get_order_details())

    # Check most aficionado
    print("Most aficionado for Latte:", Customer.most_aficionado(latte))
    print("Most aficionado for Cappuccino:", Customer.most_aficionado(cappuccino))

    # Check Coffee stats
    print("Latte num orders:", latte.num_orders())
    print("Cappuccino num orders:", cappuccino.num_orders())
    print("Cappuccino average price:", cappuccino.average_price())

if __name__ == "__main__":
    main()
