import unittest
from customer import Customer
class TestCustomer(unittest.TestCase):
    class Order:
        def __init__(self, order_id, total_price):
            self.order_id = order_id
            self.total_price = total_price

    def setUp(self):
        """Postavljanje početnih vrednosti pre svakog testa."""
        self.customer = Customer(1, "Petar Petrović", "0123456789", "Bulevar kralja Aleksandra 73", "petar@example.com")

    def test_customer_initialization(self):
        """Testira inicijalizaciju Customer objekta."""
        self.assertEqual(self.customer.customer_id, 1)
        self.assertEqual(self.customer.name, "Petar Petrović")
        self.assertEqual(self.customer.phone, "0123456789")
        self.assertEqual(self.customer.address, "Bulevar kralja Aleksandra 73")
        self.assertEqual(self.customer.email, "petar@example.com")
        self.assertEqual(self.customer.orders, [])

    def test_place_order(self):
        """Testira dodavanje narudžbine pomoću place_order metode."""
        order = self.Order(order_id=101, total_price=2500)
        self.customer.place_order(order)
        
        self.assertEqual(len(self.customer.orders), 1)  # Proverava da je narudžbina dodata
        self.assertEqual(self.customer.orders[0].order_id, 101)  # Proverava ID narudžbine
        self.assertEqual(self.customer.orders[0].total_price, 2500)  # Proverava ukupnu cenu narudžbine

    def test_get_order_history(self):
        """Testira dohvatanje istorije narudžbina pomoću get_order_history metode."""
        order1 = self.Order(order_id=101, total_price=2500)
        order2 = self.Order(order_id=102, total_price=3500)
        
        self.customer.place_order(order1)
        self.customer.place_order(order2)
        
        order_history = self.customer.get_order_history()
        self.assertEqual(len(order_history), 2)  # Proverava broj narudžbina
        self.assertEqual(order_history[0].order_id, 101)
        self.assertEqual(order_history[1].order_id, 102)

if __name__ == '__main__':
    unittest.main()
