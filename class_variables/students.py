# class variables-can be shared among all the objects within class 
#                 they are common among all the objects not like instance variable which is different according to objects


class Students:

    pass_year=2026
    students_no=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Students.students_no+=1