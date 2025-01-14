import pytest
from inventory import Inventory
from book import Textbook

def test_add_book_to_inventory():
    inventory = Inventory()
    book = Textbook("Physics Basics", "Author X", 50, 3, "Physics", "High School")
    initial_count = len(inventory.books)
    inventory.add_book(book)
    assert len(inventory.books) == initial_count + 1
    assert inventory.books[-1] == book
