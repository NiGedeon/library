class Book:
    def __init__(self, title, author):
        self.title = title   
        self.author = author  
        self._is_checked_out = False  
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self._books = []  
    
    def add_book(self, book):
        self._books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book}")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book}")
                else:
                    print(f"'{title}' wasn't checked out.")
                return
        print(f"'{title}' not found in the library.")
    
    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for boo in available_books:
                print(f"- '{boo.title}' written by '{boo.author}'")
        else:
            print("No available books at the moment.")
