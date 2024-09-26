class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position


    def describe(self):
        return(f"{self.name}={self.position}")
    

    @staticmethod
    def values(position):
        jobs=["Cook","Janitor","Manager"]
        return position in jobs
    

print(Employee.values("Cooker"))

lists=[Employee("one","manager"),Employee("two","staff"),Employee("three","cashier")]

for num in lists:
    print(num.describe())