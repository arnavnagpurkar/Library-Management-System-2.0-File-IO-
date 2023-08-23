
software_version = 2.0

# Empty lists
authors = []
books = []

# Needed Variables
library1_name = "Arnav's Library"

# Library class
class Library:


    # Start code
    def __init__(self):
        self.name = input("Enter your name: ")
        print("1. Add book")
        print("2. View added books")
        # print("3. Remove a book")
        # print("4. Remove all books")
        print("3. Exit")
        # self.choice = int(input("Enter choice(1/2/3/4/5): "))
        self.choice = int(input("Enter choice(1/2/3): "))
        if self.choice == 1 or self.choice == 2 or self.choice == 3 or self.choice == 4 or self.choice == 5:
            pass
        else:
            print("Invalid Input\nExiting...!")
            exit()

    # adding a book
    def add_book(self):
        booknum = int(input("Enter how many books you have to add: "))
        for i in range(booknum):
            print(f"\nBook number {i + 1}\n")
            book_name = input("Enter book's name: ")
            book_name = book_name.title()
            books.append(book_name)
            author_name = input("Enter author's name: ")
            author_name = author_name.title()
            authors.append(author_name)
            print(f'Book "{book_name}" written by "{author_name}" added successfully!')

    # viewing the added books
    def view_added_books(self):
        print("Your books: \n")
        for index, book in enumerate(books):
            print(f"{index + 1}. {book}")

    # removing a book
    def remove_book(self):
        print("-----------------------------------------------------")
        print("Warning: This will only remove ONE book from your added list")
        print("-----------------------------------------------------")
        print("Your books: \n")
        for index, book in enumerate(books):
            print(f"{index + 1}. {book}")
        removeinp = int(input("Enter the book number that you want to remove: "))
        del books[removeinp - 1]
        del authors[removeinp - 1]
        print("Book remove successfully!\n")

# Creating a Library using class Library.
print(f"Welcome to Library Management System {software_version} of {library1_name}.")
arnavsLibrary = Library()

# basic file io tasks
with open(f"{arnavsLibrary.name}.txt", "x") as file00:
    file00.close()
with open(f"{arnavsLibrary.name}.txt", "w") as file:
    file.write(f"Details from {library1_name} user: {arnavsLibrary.name}\n\n")

# Library Functions
if arnavsLibrary.choice == 1:
    print("\nFill the information to add the books!")
    arnavsLibrary.add_book()
    with open(f"{arnavsLibrary.name}.txt", "a") as file:
        file.write("Borrowed books:-\n")

        for i in range(len(books)):
            file.write(f"{i+1}. {books[i]} (Author - {authors[i]})\n")

    print("\n1. View added books")
    print("2. Exit")
    choice = int(input("Enter choice(1/2): "))
    # view added books
    if choice == 1:
        arnavsLibrary.view_added_books()

    # exit
    elif choice == 2:
        print(f"Printed all the details to {arnavsLibrary.name}.txt")
        print(f"Thanks for using {library1_name}!\nExiting...!")
        exit()


# if view added books
elif arnavsLibrary.choice == 2:
    arnavsLibrary.view_added_books()
    if books:
        print(f"Printed all the details to {arnavsLibrary.name}.txt")
        print(f"Thanks for using {library1_name}!\nExiting...!")
        exit()
    else:
        print("No books added!\nExiting...!")
        exit()


# exit
elif arnavsLibrary.choice == 3:
    print(f"Thanks for using {library1_name}!\nExiting...!")
    exit()

# Invalid input
else:
    print("Invalid Input!\nExiting...!")
    exit()

# End...
