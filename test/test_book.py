import unittest
from book import Book, Textbook, PictureBook, Novel
import unittest

class TestBookClasses(unittest.TestCase):
    def test_textbook_creation(self):
        """Testira kreiranje objekta Textbook i njegove atribute."""
        textbook = Textbook("Mathematics 101", "John Doe", 1500, 20, "Mathematics", "Undergraduate")
        
        self.assertEqual(textbook.title, "Mathematics 101")
        self.assertEqual(textbook.author, "John Doe")
        self.assertEqual(textbook.price, 1500)
        self.assertEqual(textbook.quantity, 20)
        self.assertEqual(textbook.subject, "Mathematics")
        self.assertEqual(textbook.academic_level, "Undergraduate")

    def test_picturebook_creation(self):
        """Testira kreiranje objekta PictureBook i njegove atribute."""
        picture_book = PictureBook("The Little Prince", "Antoine de Saint-Exupéry", 800, 30, "Antoine de Saint-Exupéry", "6+")
        
        self.assertEqual(picture_book.title, "The Little Prince")
        self.assertEqual(picture_book.author, "Antoine de Saint-Exupéry")
        self.assertEqual(picture_book.price, 800)
        self.assertEqual(picture_book.quantity, 30)
        self.assertEqual(picture_book.illustrator, "Antoine de Saint-Exupéry")
        self.assertEqual(picture_book.recommended_age, "6+")

    def test_novel_creation(self):
        """Testira kreiranje objekta Novel i njegove atribute."""
        novel = Novel("To Kill a Mockingbird", "Harper Lee", 1200, 15, "Fiction", True)
        
        self.assertEqual(novel.title, "To Kill a Mockingbird")
        self.assertEqual(novel.author, "Harper Lee")
        self.assertEqual(novel.price, 1200)
        self.assertEqual(novel.quantity, 15)
        self.assertEqual(novel.genre, "Fiction")
        self.assertTrue(novel.is_bestseller)

    def test_textbook_get_details(self):
        """Testira da li metoda get_details za Textbook vraća ispravne informacije."""
        textbook = Textbook("Physics for Engineers", "Alice Smith", 1800, 10, "Physics", "Graduate")
        self.assertEqual(textbook.get_details(), "Physics for Engineers by Alice Smith - Physics (Graduate)")

    def test_picturebook_get_details(self):
        """Testira da li metoda get_details za PictureBook vraća ispravne informacije."""
        picture_book = PictureBook("Winnie the Pooh", "A. A. Milne", 900, 40, "Ernest H. Shepard", "5+")
        self.assertEqual(picture_book.get_details(), "Winnie the Pooh by A. A. Milne, illustrated by Ernest H. Shepard - Recommended for age 5+")

    def test_novel_get_details(self):
        """Testira da li metoda get_details za Novel vraća ispravne informacije."""
        novel = Novel("1984", "George Orwell", 1000, 25, "Dystopian", False)
        self.assertEqual(novel.get_details(), "1984 by George Orwell - Genre: Dystopian ")

    def test_book_abstract_class(self):
        """Testira da li je Book apstraktna klasa i da li izaziva grešku prilikom instanciranja."""
        with self.assertRaises(TypeError):
            Book("Some Title", "Some Author", 100, 10)  # Ovo bi trebalo izazvati grešku jer je Book apstraktna klasa

if __name__ == '__main__':
    unittest.main()
