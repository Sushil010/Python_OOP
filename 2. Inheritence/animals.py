# class children(Parent)



class Animals:
    def __init__(self,name):
        self.name=name
        self.alive=True

    def Eat(self):
        print(f"{self.name} is eating")

    def walking(self):
        print(f"{self.name} is walking")