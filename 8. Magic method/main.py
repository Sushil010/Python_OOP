class Books:

    def __init__(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages

    def __str__(self):
        return(f"{self.name} is written by {self.author}")
    

    def __eq__(self, other):
        return(self.name==other.name)
    
    def __lt__(self,other):
        return(self.pages < other.pages)
    
    def __gt__(self,other):
        return(self.pages>other.pages)

    def __contains__(self,key):
        return(key in self.name)
    
    def __getitem__(self,key):
        if key=="name":
            return self.name
        elif key=="author":
            return self.author
        elif key=="pages":
            return self.pages    
        else:
            return("Not contained")

book1=Books("Some random book","Author1",234)
book2=Books("Another random one","Author2",74)
book3=Books("No idea about name","Authorinfinite",999)
book4=Books("Some random book","Author1",234)


# print(book1)
# print(book3)
# print(book1==book2)

# print(book1 < book3)
# print(book1>book2)


# print("No" in book3 )
print(book3["name"])