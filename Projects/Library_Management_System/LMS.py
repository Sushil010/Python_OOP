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

