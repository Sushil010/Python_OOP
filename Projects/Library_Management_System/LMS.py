print("Library Management System")

class Book:
    def __init__(self,title,author,id,copies):
        self.title=title
        self.author=author
        self.id=id
        self.copies=copies
    
    # changes--provide the book name according to id of the book
    def display_details(self):
        print(f"Book name is {self.title} and author is {self.author}")

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
        self.bookss=books
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
        pass




