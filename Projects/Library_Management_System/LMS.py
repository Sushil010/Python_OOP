print("Library Management System")

class Book:
    def __init__(self,title,author,id,copies):
        self.title=title
        self.author=author
        self.id=id
        self.copies=copies
    
    # changes--provide the book name according to id of the book
    def display_details(self):
        # print(f"Available book is {book[id]}. {book['title'] } by {book['author']} and remaining {book['copies']}")
        print(f"{self.id}. Book name is {self.title} and author is {self.author} with remaining copies {self.copies}")

    def update_copies(self):
        pass


class Individual:
    def __init__(self, name, member_id, borrowed_books):
        self.name=name
        self.member_id=member_id
        self.borrowed_books=borrowed_books
    
    def borrow_books(self,book_id):
        pass

    def return_book(self, book_id):
        pass


class Library:
    def __init__(self,books,members):
        self.books=books
        self.members=members
    
    def add_book(self,book_id):
        pass

    def remove_book(self,book_obj):
        pass

    def register_member(self,member_obj):
        pass

    def issue_book(self, book_id,member_id):
        pass

    def return_book(self, member_id, bokk_id):
        pass

    def list_available_books(self):
        for book in self.books:
            print(f"{book['id']}. Title of book is {book['title']} written by {book['author']}")
        
        



books=[
    {"id":1,"title":"Three body Problem", "author":"Unknown","copies":3},
    {"id":2,"title":"Harry Potter and the goblet of fire", "author":"JK.Rowling","copies":5}
]

members=[
    {"id":1,"name":"Sushil Sharma"},
    {"id":2,"name":"John Doe"}
]


# this library class consists of whole lists and objects passed within it so itertion is required within it's methods
Lib=Library(books,members)
Lib.list_available_books()

# only a specific portion of an object-list is passed so 

book_obj=[Book(book["title"],book["author"],book["id"],book["copies"]) for book in books]

# iteration inside method of this is redundant so iteration is done in this way
for book in book_obj:
    book.display_details()
