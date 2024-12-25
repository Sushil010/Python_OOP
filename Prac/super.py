class Parent1:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def describe(self):
        print("from parent class")

class children1(Parent1):
    def __init__(self,name,color,height):
        super().__init__(name,color)
        self.height=height


    def describe(self):
        super().describe()
        print("from children class")

# flow is first paramater reach to children and only to parent
# useful when parameters need to change before passing to Parent class

c1=children1("circle","green",20)
c1.describe()
