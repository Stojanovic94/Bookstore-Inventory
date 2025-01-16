from book import Textbook, PictureBook, Novel
from inventory import Inventory
from order import Order
from customer import Customer

# Osnove
inventory = Inventory()
book1 = Textbook("Math Basics", "Author A", 100, 10, "Math", "High School")
book2 = PictureBook("Animal World", "Author B", 150, 5, "Illustrator A", 5)
book3 = Novel("Mystery Novel", "Author C", 200, 3, "Thriller", True)

inventory.add_book(book1)
inventory.add_book(book2)
inventory.add_book(book3)

customer = Customer(1, "John Doe", "123-456", "123 Main St", "john@example.com")
order = Order(1)
order.add_book_to_order(book1)
customer.place_order(order)

print(inventory.display_inventory())
print(customer.get_order_history())
