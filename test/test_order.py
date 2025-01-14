import unittest
from order import Order

class TestOrder(unittest.TestCase):
    class Book:
        def __init__(self, price):
            self.price = price

    def setUp(self):
        """Postavljanje početnih vrednosti pre svakog testa."""
        self.order = Order(1)  # Inicijalizacija objekta Order

    def test_initial_order(self):
        """Testira inicijalnu vrednost narudžbine."""
        self.assertEqual(self.order.order_id, 1)  # Proverava id narudžbine
        self.assertEqual(self.order.books, [])  # Proverava da li je lista knjiga prazna
        self.assertEqual(self.order.total_price, 0)  # Proverava da li je ukupna cena 0

    def test_add_book_to_order(self):
        """Testira dodavanje knjige u narudžbinu."""
        book = self.Book(price=100)
        self.order.add_book_to_order(book)
        
        self.assertEqual(len(self.order.books), 1)  # Proverava da li je knjiga dodata
        self.assertEqual(self.order.books[0].price, 100)  # Proverava cenu dodate knjige
        self.assertEqual(self.order.total_price, 100)  # Proverava da li je ukupna cena tačna

    def test_calculate_total_price(self):
        """Testira tačnost izračunavanja ukupne cene."""
        book1 = self.Book(price=100)
        book2 = self.Book(price=200)
        self.order.add_book_to_order(book1)
        self.order.add_book_to_order(book2)
        
        self.assertEqual(self.order.total_price, 300)  # Proverava ukupnu cenu (100 + 200)

    def test_empty_order_total_price(self):
        """Testira da li ukupna cena ostaje 0 ako nema knjiga u narudžbini."""
        self.assertEqual(self.order.total_price, 0)  # Proverava da li je ukupna cena 0 za praznu narudžbinu

if __name__ == '__main__':
    unittest.main()
