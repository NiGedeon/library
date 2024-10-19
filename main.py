import os
import time
from library import Book,Library
def menu():
    print("Press 1 to add a book")
    print("Press 2 to check for available books")
    print("Press 3 to check out a book")
    print("Press 4 to return a book")
    print("Press 0 to exit")

def main():
    library = Library()

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        menu()
        try:
            choice = int(input("\n\tEnter your Choice : "))
          
        except ValueError:
            print("Invalid input! Please enter a number.")
            time.sleep(2)  
            continue

        if choice == 1:
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            library.add_book(Book(title, author))
        elif choice == 2:
            print("Available books:")
            library.list_available_books()
        elif choice == 3:
            title = input("Enter the title of the book to check out: ")
            library.check_out_book(title)
            print("\nAvailable books after checking out:")
            library.list_available_books()
        elif choice == 4:
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
            print("\nAvailable books after returning:")
            library.list_available_books()
        elif choice == 0:
            break
        else:
            print("Invalid Choice\n")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
