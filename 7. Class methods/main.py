class Students:
    student_count=0
    total_gpa=0


    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Students.student_count+=1
        Students.total_gpa+=self.gpa

    def students(self):
        return(f"{self.name} got {self.gpa}")
    

    @classmethod
    def data(cls):
        return(f"Total students are: {cls.student_count}")

    @classmethod
    def avg_gpa(cls):
        return(f"Average gpa obtained is: {cls.total_gpa/cls.student_count:.2f}")


std1=Students("stdone",2.0)
std2=Students("stdtwo",3.0)
std3=Students("stdthree",3.3)
std4=Students("stdfour",3.9)

print(Students.data())
print(Students.avg_gpa())