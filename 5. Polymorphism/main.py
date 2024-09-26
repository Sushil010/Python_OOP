
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return(self.radius*self.radius*3.14)



class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return(self.base*self.height*1/2)


class Prism(Triangle):
    def __init__(self, base, height,toppings):
        self.toppings=toppings
        super().__init__(base, height)
        
    def returned(self):
        return(self.toppings)
    


circle=Circle(20)
triangle=Triangle(20,30)
prism=Prism(50,60,"topp")


shapes=[circle,triangle,prism]

# print(prism.area(),prism.returned())


for shape in shapes:
    print(shape.area())