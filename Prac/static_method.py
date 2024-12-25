class First:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def ps(self):
        print ("f{self.name}={self.position}")

    @staticmethod
    def independent(post):
        value=["one","two","three"]
        return post in value

print(First.independent("two"))