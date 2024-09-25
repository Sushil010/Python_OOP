# multiple inheritence - inherit from more than one parent class 
#                          C(A,B)



# multilevel inheritence- inherit from one parent that inherit from another parent


# class Animal:
#     def __init__(self,name):
#         self.name=name

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


class one:
    def inone(self):
        print("inside of one")


class two:
    def intwo(self):
        print("inside of two")


class three:
    def inthree(self):
        print("Inside of three")


class two(one):
    pass

class three(two):
    pass


Two=two()
Two.inone()


Three=three()
Three.inone()