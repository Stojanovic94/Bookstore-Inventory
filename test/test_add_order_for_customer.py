from customer import Customer
from order import Order

def test_add_order_for_customer():
    customer = Customer(1, "Jane Doe", "555-1234", "123 Elm St", "jane@example.com")
    order = Order(1)
    initial_order_count = len(customer.orders)
    customer.place_order(order)
    assert len(customer.orders) == initial_order_count + 1
    assert customer.orders[-1] == order
