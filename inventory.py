class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_inventory(self):
        return [book.get_details() for book in self.books]
