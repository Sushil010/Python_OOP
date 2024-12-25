class Parent1:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class children1(Parent1):
    def __init__(self,name,color,height):
        super().__init__(name,color)
        self.height=height


# flow is first paramater reach to children and only to parent
# useful when parameters need to change before passing to Parent class

c1=children1("circle","green",20)
