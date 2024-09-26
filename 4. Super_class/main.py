class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"It is {self.color} with {'filled' if self.is_filled else 'not_filled'}")


class circle(Shape):
    def __init__(self,color,is_filled,radius):
        # self.color=color
        # self.is_filled=is_filled
        super().__init__(color,is_filled)
        self.radius=radius

    #method overriding  
    def describe(self):
        print(f"The area is {self.radius*self.radius*3.14} cm^2")
        # accessing parent or super class even overriding the method:
        super().describe()

    

class square(Shape):
    def __init__(self,color,is_filled,length):
        # self.color=color
        # self.is_filled=is_filled
        super().__init__(color,is_filled)
        self.length=length
        


class triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        # self.color=color
        # self.is_filled=is_filled
        super().__init__(color,is_filled)
        self.width=width
        self.height=height


Circle=circle("green",True,10)
# print(f"Circle is {Circle.color} with {Circle.is_filled} and geometry {Circle.radius}")


Triangle=triangle("yellow",False,100,200)
# print(f"Triangle is {Triangle.color} with {Triangle.is_filled} and geometry {Triangle.width} and {Triangle.height}")

Square=square("purple",True,90)
# print(f"Square is {Square.color} with {Square.is_filled} and geometry {Square.length}")


Circle.describe()
# Triangle.describe()