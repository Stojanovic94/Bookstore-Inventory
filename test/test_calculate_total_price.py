from order import Order
from book import Textbook

def test_calculate_total_price():
    order = Order(1)
    book1 = Textbook("Math Basics", "Author A", 100, 2, "Math", "College")
    book2 = Textbook("Science Basics", "Author B", 150, 1, "Science", "High School")
    order.add_book_to_order(book1)
    order.add_book_to_order(book2)
    assert order.total_price == 250
