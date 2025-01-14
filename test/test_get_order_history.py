def test_get_order_history():
    customer = customer(2, "John Smith", "555-5678", "456 Maple Ave", "john@example.com")
    order1 = order1(1)
    order2 = order1(2)
    customer.place_order(order1)
    customer.place_order(order2)
    order_history = customer.get_order_history()
    assert len(order_history) == 2
    assert order_history[0] == order1
    assert order_history[1] == order2
