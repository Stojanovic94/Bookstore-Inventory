class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.books = []
        self.total_price = 0

    def add_book_to_order(self, book):
        self.books.append(book)
        self.calculate_total_price()

    def calculate_total_price(self):
        self.total_price = sum(book.price for book in self.books)
