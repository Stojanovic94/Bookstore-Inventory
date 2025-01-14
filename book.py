from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass

class Textbook(Book):
    def __init__(self, title, author, price, quantity, subject, academic_level):
        super().__init__(title, author, price, quantity)
        self.subject = subject
        self.academic_level = academic_level

    def get_details(self):
        return f"{self.title} by {self.author} - {self.subject} ({self.academic_level})"

class PictureBook(Book):
    def __init__(self, title, author, price, quantity, illustrator, recommended_age):
        super().__init__(title, author, price, quantity)
        self.illustrator = illustrator
        self.recommended_age = recommended_age

    def get_details(self):
        return f"{self.title} by {self.author}, illustrated by {self.illustrator} - Recommended for age {self.recommended_age}"

class Novel(Book):
    def __init__(self, title, author, price, quantity, genre, is_bestseller):
        super().__init__(title, author, price, quantity)
        self.genre = genre
        self.is_bestseller = is_bestseller

    def get_details(self):
        bestseller_status = "Bestseller" if self.is_bestseller else ""
        return f"{self.title} by {self.author} - Genre: {self.genre} {bestseller_status}"
