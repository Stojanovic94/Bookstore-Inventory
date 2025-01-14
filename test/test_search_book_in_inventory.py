def test_search_book_in_inventory():
    inventory = Inventory()
    book = Textbook("Biology Basics", "Author C", 75, 4, "Biology", "High School")
    inventory.add_book(book)
    result = inventory.search_book("Biology Basics")
    assert result == book
    assert result.title == "Biology Basics"
