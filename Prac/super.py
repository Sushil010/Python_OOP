class Parent1:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class children1(Parent1):
    def first(self,height):
        super().__init__(name,color)
        self.height=height
