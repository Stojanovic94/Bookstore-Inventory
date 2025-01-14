import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):
    class Book:
        def __init__(self, title, author, price, quantity):
            self.title = title
            self.author = author
            self.price = price
            self.quantity = quantity

        def get_details(self):
            return f"{self.title} by {self.author} - Price: {self.price} - Quantity: {self.quantity}"

    def setUp(self):
        """Postavljanje početnih vrednosti pre svakog testa."""
        self.inventory = Inventory()
        self.book1 = self.Book("Python Programming", "Guido van Rossum", 1000, 5)
        self.book2 = self.Book("Data Science Essentials", "Alice Smith", 1500, 3)

    def test_inventory_initialization(self):
        """Testira inicijalizaciju Inventory objekta."""
        self.assertEqual(self.inventory.books, [])

    def test_add_book(self):
        """Testira dodavanje knjige u inventar pomoću add_book metode."""
        self.inventory.add_book(self.book1)
        self.assertIn(self.book1, self.inventory.books)  # Proverava da li je knjiga dodata

    def test_remove_book(self):
        """Testira uklanjanje knjige iz inventara pomoću remove_book metode."""
        self.inventory.add_book(self.book1)
        self.inventory.remove_book(self.book1)
        self.assertNotIn(self.book1, self.inventory.books)  # Proverava da li je knjiga uklonjena

    def test_search_book(self):
        """Testira pretragu knjige po naslovu pomoću search_book metode."""
        self.inventory.add_book(self.book1)
        self.inventory.add_book(self.book2)
        found_book = self.inventory.search_book("Python Programming")
        self.assertEqual(found_book, self.book1)  # Proverava da li je pronađena odgovarajuća knjiga

        not_found_book = self.inventory.search_book("Nonexistent Book")
        self.assertIsNone(not_found_book)  # Proverava da li je rezultat None za nepostojeću knjigu

    def test_display_inventory(self):
        """Testira prikaz inventara pomoću display_inventory metode."""
        self.inventory.add_book(self.book1)
        self.inventory.add_book(self.book2)
        display = self.inventory.display_inventory()
        expected_display = [
            "Python Programming by Guido van Rossum - Price: 1000 - Quantity: 5",
            "Data Science Essentials by Alice Smith - Price: 1500 - Quantity: 3"
        ]
        self.assertEqual(display, expected_display)  # Proverava da li je prikaz inventara tačan

if __name__ == '__main__':
    unittest.main()
