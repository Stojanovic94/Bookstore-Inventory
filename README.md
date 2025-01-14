# Bookstore Inventory Management System

This repository contains a system for managing and tracking inventory in a bookstore. It includes functionalities for managing books, customers, and orders. The system supports adding books to inventory, processing orders, and managing customer information. The design employs object-oriented principles, such as aggregation and composition, to manage relationships between classes.

## Features

- **Book Management**: Add and manage different types of books such as textbooks, picture books, and novels.
- **Inventory Management**: Keep track of the available books in the inventory, including adding, removing, and searching books.
- **Order Management**: Customers can place orders for books, and the system calculates the total price based on the books in the order.
- **Customer Management**: Customers can place orders, and their order history is tracked.

## Classes Overview

### `Book` (Abstract Class)
The `Book` class serves as a base for different types of books. It contains:
- `title`: The title of the book.
- `author`: The author of the book.
- `price`: The price of the book.
- `quantity`: The available quantity of the book.

Methods:
- `get_details()`: Returns the details of the book.

### `Textbook`, `PictureBook`, `Novel` (Subclasses of Book)
These classes represent specific types of books:
- `Textbook`: Academic books with additional attributes like subject.
- `PictureBook`: Children's books with illustrations.
- `Novel`: Fictional works.

### `Inventory`
The `Inventory` class is responsible for managing the collection of books in the bookstore.
- `books`: A list of books in the inventory.

Methods:
- `add_book(book)`: Adds a book to the inventory.
- `remove_book(book)`: Removes a book from the inventory.
- `search_book(title)`: Searches for a book by its title in the inventory.
- `get_book_count()`: Returns the total number of books in the inventory.

### `Order`
The `Order` class represents a customer's order. It includes:
- `order_id`: A unique identifier for the order.
- `books`: A list of books in the order.
- `total_price`: The total price of the order.

Methods:
- `add_book(book)`: Adds a book to the order.
- `calculate_total()`: Calculates the total price of the order.

### `Customer`
The `Customer` class represents a customer in the system. It contains:
- `name`: The name of the customer.
- `email`: The email address of the customer.
- `orders`: A list of orders placed by the customer.

Methods:
- `place_order(order)`: Places an order for the customer.
- `get_order_history()`: Retrieves the customer's order history.
